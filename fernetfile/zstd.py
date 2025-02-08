# -*- encoding: utf-8 -*-
""" Fast and furious FernetFile interface.
It uses the multithreaded ZSTD compressor.

"""
__license__ = """
    All rights reserved by Labo-Online
"""
__copyright__ = "Copyright ©2024-2025 "
__author__ = 'bibi21000 aka Sébastien GALLET'
__email__ = 'bibi21000@gmail.com'

import os
import sys
import io

import fernetfile
from fernetfile import CHUNK_SIZE, READ, WRITE, APPEND, EXCLUSIVE # noqa F401

try:
    import pyzstd
    from pyzstd import CParameter, DParameter # noqa F401

    class FernetFile(pyzstd.ZstdFile):

        def __init__(self, name, mode='r', fernet_key=None, level_or_option=None, zstd_dict=None, **kwargs):
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

            level_or_option is a dict for ztsd compressions.
            2 parameters are importants for performances and cpu usage when writing:

              - compressionLevel
              - nbWorkers

            Look at `pyzstd documentation <https://pyzstd.readthedocs.io/en/stable/#advanced-parameters>`_
            """
            chunk_size = kwargs.pop('chunk_size', CHUNK_SIZE)
            self.fernet_file = fernetfile.FernetFile(name, mode,
                fernet_key=fernet_key, chunk_size=chunk_size, **kwargs)
            try:
                super().__init__(self.fernet_file, zstd_dict=zstd_dict,
                    level_or_option=level_or_option, mode=mode, **kwargs)
            except Exception:
                self.fernet_file.close()
                raise

        def __repr__(self):
            s = repr(self.fernet_file)
            return '<ZstdFernetFile ' + s[1:-1] + ' ' + hex(id(self)) + '>'


        def close(self):
            try:
                super().close()
            finally:
                if self.fernet_file is not None:
                    self.fernet_file.close()

    def open(filename, mode="rb", fernet_key=None,
            encoding=None, errors=None, newline=None,
            chunk_size=CHUNK_SIZE,
            level_or_option=None, zstd_dict=None):
        """Open a ZstdFernet file in binary or text mode.

        The filename argument can be an actual filename (a str or bytes object), or
        an existing file object to read from or write to.

        The mode argument can be "r", "rb", "w", "wb", "x", "xb", "a" or "ab" for
        binary mode, or "rt", "wt", "xt" or "at" for text mode. The default mode is
        "rb".

        For binary mode, this function is equivalent to the FernetFile constructor:
        FernetFile(filename, mode, fernet_key). In this case, the encoding, errors
        and newline arguments must not be provided.

        For text mode, a FernetFile object is created, and wrapped in an
        io.TextIOWrapper instance with the specified encoding, error handling
        behavior, and line ending(s).

        Encryption is done by chunks to reduce memory footprint. The default
        chunk_size is 64KB.

        level_or_option is a dict for ztsd compressions.
        2 parameters are importants for performances and cpu usage when writing :

          - compressionLevel
          - nbWorkers

        Look at `pyzstd documentation <https://pyzstd.readthedocs.io/en/stable/#advanced-parameters>`_

        """
        if "t" in mode:
            if "b" in mode:
                raise ValueError("Invalid mode: %r" % (mode,))
        else:
            if encoding is not None:
                raise ValueError("Argument 'encoding' not supported in binary mode")
            if errors is not None:
                raise ValueError("Argument 'errors' not supported in binary mode")
            if newline is not None:
                raise ValueError("Argument 'newline' not supported in binary mode")

        frnt_mode = mode.replace("t", "")
        if isinstance(filename, (str, bytes, os.PathLike)):
            binary_file = FernetFile(filename, mode=frnt_mode, fernet_key=fernet_key, chunk_size=chunk_size,
                level_or_option=level_or_option, zstd_dict=zstd_dict)
        elif hasattr(filename, "read") or hasattr(filename, "write"):
            binary_file = FernetFile(None, mode=frnt_mode, fernet_key=fernet_key, fileobj=filename,
                chunk_size=chunk_size, level_or_option=level_or_option, zstd_dict=zstd_dict)
        else:
            raise TypeError("filename must be a str or bytes object, or a file")

        if "t" in mode:
            if hasattr(io, "text_encoding"):
                text_encoding = io.text_encoding
            else:
                # For python 3.9
                def text_encoding(encoding) -> str:
                    if encoding is not None:
                        return encoding
                    if sys.flags.utf8_mode:
                        return "utf-8"
                    return "locale"
            encoding = text_encoding(encoding)
            return io.TextIOWrapper(binary_file, encoding, errors, newline)
        else:
            return binary_file


except ModuleNotFoundError:
    raise ModuleNotFoundError("Install fernetfile with [zstd] extras")
