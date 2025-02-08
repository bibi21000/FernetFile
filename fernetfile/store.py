# -*- encoding: utf-8 -*-
""" Store your files in a ztsd/tar based archive.

2 versions :

Encrypted tar

Encrypted tar of encrypted files

Interface "compatible" with tar :

- open :
    - decrompress and extract files in a temporary directory

=> need to be thread safe (flush can be called from another thread)

"""
__license__ = """
    All rights reserved by Labo-Online
"""
__copyright__ = "Copyright ©2024-2025 "
__author__ = 'bibi21000 aka Sébastien GALLET'
__email__ = 'bibi21000@gmail.com'

import os
import time
import tempfile
import threading
from contextlib import contextmanager
import shutil
import tarfile
import io
from filelock import FileLock

from fernetfile.zstd import FernetFile as ZstdFernetFile
from fernetfile.zstd import CHUNK_SIZE, READ, WRITE, APPEND, EXCLUSIVE


class TarZstdFernetFile(tarfile.TarFile):
    """ """

    def __init__(self, name, mode='r', fernet_key=None, **kwargs):
        """ """
        level_or_option = kwargs.pop('level_or_option', None)
        zstd_dict = kwargs.pop('zstd_dict', None)
        chunk_size = kwargs.pop('chunk_size', CHUNK_SIZE)
        self.fernet_file = ZstdFernetFile(name, mode,
            fernet_key=fernet_key, level_or_option=level_or_option,
                zstd_dict=zstd_dict, chunk_size=chunk_size, **kwargs)
        try:
            super().__init__(fileobj=self.fernet_file, mode=mode.replace('b', ''), **kwargs)

        except Exception:
            self.fernet_file.close()
            raise

    def close(self):
        """ """
        try:
            super().close()

        finally:
            if self.fernet_file is not None:
                self.fernet_file.close()

    def __repr__(self):
        """ """
        s = repr(self.fernet_file)
        return '<TarZstdFernet ' + s[1:-1] + ' ' + hex(id(self)) + '>'


class StoreInfo():
    """ """

    def __init__(self, name, store_path=None):
        """ """
        self.store_path = store_path
        sname = str(name)
        if sname[0] == '/':
            self.name = sname[1:]
        else:
            self.name = sname
        dirs = self.name.rsplit('/', 1)
        if len(dirs) > 1 :
            self.subdir = os.path.join(self.store_path, '%s'%dirs[0])
            self.dirpath = os.path.join(self.store_path, self.subdir)
        else:
            self.subdir = None
            self.dirpath = self.store_path
        self.path = os.path.join(self.store_path, '%s'%self.name)

    @property
    def mtime(self):
        """ """
        if os.path.isfile(self.path):
            return os.path.getmtime(self.path)
        return None

    def __repr__(self):
        """ """
        s = repr(self.name)
        return '<FernetStoreInfo ' + s[1:-1] + ' ' + hex(id(self)) + '>'

class FernetStore():
    """ """

    def __init__(self, filename=None, mode=None, fernet_key=None,
            secure_open=None, auto_flush=True, backup=None, **kwargs):
        """Constructor for the FernetFile class.

        At least one of fileobj and filename must be given a
        non-trivial value.

        The new class instance is based on fileobj, which can be a regular
        file, an io.BytesIO object, or any other object which simulates a file.
        It defaults to None, in which case filename is opened to provide
        a file object.

        When fileobj is not None, the filename argument is only used to be
        included in the gzip file header, which may include the original
        filename of the uncompressed file.  It defaults to the filename of
        fileobj, if discernible; otherwise, it defaults to the empty string,
        and in this case the original filename is not included in the header.

        The mode argument can be any of 'r', 'rb', 'a', 'ab', 'w', 'wb', 'x', or
        'xb' depending on whether the file will be read or written.  The default
        is the mode of fileobj if discernible; otherwise, the default is 'rb'.
        A mode of 'r' is equivalent to one of 'rb', and similarly for 'w' and
        'wb', 'a' and 'ab', and 'x' and 'xb'.

        The fernet_key argument is the Fernet key used to crypt/decrypt data.
        Encryption is done by chunks to reduce memory footprint. The default
        chunk_size is 64KB.

        Files are stored in clear mode when opening archive (in a directory in /tmp).
        You can give a "secured open" command to avoid that (in dev)

        Everytime data are written in archive, it is flushed to file : this means
        that thar archive is compressed and crypted. You can change this with auto_flush.
        Data will be flushed only on close.

        If you want to backup archive before flushing it, pass extention to this parameter.
        """
        if fernet_key is None:
            raise ValueError("Invalid fernet key: {!r}".format(fernet_key))
        if filename is None:
            raise ValueError("Invalid filename: {!r}".format(filename))
        if mode is None or ('t' in mode or 'U' in mode):
            raise ValueError("Invalid mode: {!r}".format(mode))
        if mode and 'b' not in mode:
            mode += 'b'
        if mode.startswith('r'):
            self.mode = READ
        elif mode.startswith('w'):
            self.mode = WRITE
        elif mode.startswith('a'):
            self.mode = APPEND
        elif mode.startswith('x'):
            self.mode = EXCLUSIVE
        else:
            raise ValueError("Invalid mode: {!r}".format(mode))
        self._lock = threading.Lock()
        self.fernet_key = fernet_key
        self.kwargs = kwargs
        self.filename = filename
        self.backup = backup
        self.auto_flush = auto_flush
        self._lockfile = FileLock(self.filename+'.lock')
        self.secure_open = open
        if secure_open is not None:
            self.secure_open = secure_open
        self.dirpath = None
        self._dirctime = None
        self._dirmtime = None

    def __repr__(self):
        """ """
        s = repr(self.filename)
        return '<FernetStore ' + s[1:-1] + ' ' + hex(id(self)) + '>'

    def _check_not_closed(self):
        """ """
        if self.closed:
            raise io.UnsupportedOperation("I/O operation on closed file")

    def _check_can_write(self):
        """ """
        if self.closed:
            raise io.UnsupportedOperation("I/O operation on closed file")
        if not self.writable:
            raise io.UnsupportedOperation("File not open for writing")

    def __enter__(self):
        """ """
        return self.open()

    def __exit__(self, type, value, traceback):
        """ """
        self.close()

    def open(self):
        """ """
        self._lockfile.acquire()
        file_exists = os.path.isfile(self.filename)
        if file_exists:
            if self.mode == EXCLUSIVE:
                import errno
                raise FileExistsError('File already exists %s' % self.filename)
        else:
            if self.mode == READ:
                import errno
                raise FileNotFoundError('File not found %s' % self.filename)
        self.dirpath = tempfile.mkdtemp(prefix=".fernet_")
        if file_exists:
            with TarZstdFernetFile(self.filename, mode='rb', fernet_key=self.fernet_key, **self.kwargs) as tff:
                tff.extractall(self.dirpath)
        self._dirctime = self._dirmtime = time.time_ns()
        return self

    def _write_store(self):
        """ """
        self._check_can_write()
        with self._lock:
            if self.backup is not None:
                if os.path.isfile(self.filename + self.backup) is True:
                    os.remove(self.filename + self.backup)
                shutil.copy(self.filename, self.filename + self.backup)

            with TarZstdFernetFile(self.filename, mode='wb', fernet_key=self.fernet_key, **self.kwargs) as tff:
                for member in self.getmembers():
                    tff.add(member.path, arcname=member.name)

            self._dirctime = self._dirmtime = time.time_ns()

    def getmembers(self):
        """ """
        members = []
        for root, dirs, files in os.walk(self.dirpath):
            for fname in files:
                aname = os.path.join( root[len(self.dirpath):], fname )
                members.append(StoreInfo(aname, store_path=self.dirpath))
        return members

    def close(self):
        """ """
        if self.writable:
            self._write_store()
        shutil.rmtree(self.dirpath)
        self.dirpath = None
        self._dirctime = None
        self._dirmtime = None
        self._lockfile.release()

    def flush(self, force=True):
        """ """
        if force is False and self.modified is False:
            return
        self._write_store()

    @contextmanager
    def file(self, arcname=None, mode='rb', encoding=None):
        """Return a file descriptor"""
        fffile = None
        with self._lock:
            if isinstance(arcname, StoreInfo):
                finfo = arcname
            else:
                finfo = StoreInfo(arcname, store_path=self.dirpath)
            try:
                if finfo.subdir is not None:
                    os.makedirs(os.path.join(self.dirpath, finfo.subdir), exist_ok=True)
                fffile = ffile = self.secure_open(finfo.path, mode=mode, encoding=encoding)
                yield ffile
                ffile.close()
                ffile = None
                if mode.startswith(('w', 'a', 'x')):
                    self._dirmtime = time.time_ns()
            finally:
                if fffile is not None:
                    fffile.close()
                    fffile = None

        if self.auto_flush is True and mode.startswith(('w', 'a', 'x')):
            self.flush()

    def add(self, filename, arcname=None, replace=True):
        """ """
        with self._lock:
            self._check_can_write()
            if isinstance(arcname, StoreInfo):
                finfo = arcname
            else:
                finfo = StoreInfo(arcname, store_path=self.dirpath)

            file_exists = os.path.isfile(finfo.path)
            if file_exists is True and replace is False:
                import errno
                raise FileExistsError('File already exists %s' % self.filename)

            if file_exists is True:
                self._delete(arcinfo=finfo)

            if finfo.subdir is not None:
                os.makedirs(os.path.join(self.dirpath, finfo.subdir), exist_ok=True)

            with open(filename, 'rb') as ff, self.secure_open(finfo.path, mode='wb') as sf:
                sf.write(ff.read())
            self._dirmtime = time.time_ns()

        if self.auto_flush is True:
            self.flush()

    def _delete(self, arcinfo=None):
        """Delete file in store without lock"""
        self._check_can_write()
        os.remove(arcinfo.path)
        self._dirmtime = time.time_ns()

    def delete(self, arcname=None):
        """Delete file in store"""
        with self._lock:
            if isinstance(arcname, StoreInfo):
                finfo = arcname
            else:
                finfo = StoreInfo(arcname, store_path=self.dirpath)
            self._delete(arcinfo=finfo)
        if self.auto_flush is True:
            self.flush()

    def append(self, data, arcname=None):
        """ """
        self._check_can_write()
        with self.file(arcname=arcname, mode='ab') as nf:
            nf.write(data)

    def write(self, data, arcname=None):
        """ """
        self._check_can_write()
        with self.file(arcname=arcname, mode='wb') as nf:
            nf.write(data)

    def read(self, arcname=None):
        """ """
        self._check_not_closed()
        with self.file(arcname=arcname, mode='rb') as nf:
            return nf.read()

    def readlines(self, arcname=None, encoding='UTF-8'):
        """ """
        self._check_not_closed()
        lines = []
        with self.file(arcname=arcname, mode='rt', encoding=encoding) as nf:
            for line in nf:
                lines.append(line.rstrip())
        return lines

    def writelines(self, lines, arcname=None, encoding='UTF-8'):
        """ """
        self._check_can_write()
        with self.file(arcname=arcname, mode='wt', encoding=encoding) as nf:
            for line in lines:
                nf.write(line + '\n')

    @property
    def mtime(self):
        """Last modification time read from stream, or None."""
        if os.path.isfile(self.filename) is True:
            return os.path.getmtime(self.filename)
        return None

    @property
    def modified(self):
        """Archive has been updated but not flushed."""
        self._check_not_closed()
        return self._dirctime < self._dirmtime

    @property
    def closed(self):
        """True if this file is closed."""
        return self.dirpath is None

    @property
    def readable(self):
        """Return whether the file was opened for reading."""
        self._check_not_closed()
        return self.mode == READ

    @property
    def writable(self):
        """Return whether the file was opened for writing."""
        self._check_not_closed()
        return self.mode == WRITE or self.mode == APPEND \
            or self.mode == EXCLUSIVE
