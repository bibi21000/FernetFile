# -*- encoding: utf-8 -*-
""" TarFile interface.

"""
__author__ = 'bibi21000 aka Sébastien GALLET'
__email__ = 'bibi21000@gmail.com'

import os
import sys
import io
import tarfile

from cofferfile import _open_cls
from . import CHUNK_SIZE, READ, WRITE, APPEND, EXCLUSIVE # noqa F401
from .zstd import FernetFile as ZstdFernetFile, CParameter, DParameter


class TarFile(tarfile.TarFile):
    """The container of the store. Based on TarFfile with encryption"""

    def __init__(self, name, mode='r', fileobj=None,
            chunk_size=CHUNK_SIZE,
            level_or_option=None, zstd_dict=None,
            fernet_key=None, **kwargs
        ):
        """Init the TarZstdFernetFile"""
        chunk_size = kwargs.pop('chunk_size', CHUNK_SIZE)
        cryptor = kwargs.pop('cryptor', None)
        self.fernet_file = ZstdFernetFile(name, mode, fileobj=fileobj,
            fernet_key=fernet_key, level_or_option=level_or_option,
                zstd_dict=zstd_dict, chunk_size=chunk_size)
        try:
            super().__init__(fileobj=self.fernet_file, mode=mode.replace('b', ''), **kwargs)

        except Exception:
            self.fernet_file.close()
            raise

    def close(self):
        """Close the TarZstdFernetFile"""
        try:
            super().close()

        finally:
            if self.fernet_file is not None:
                self.fernet_file.close()

    def __repr__(self):
        """ """
        s = repr(self.fernet_file)
        return '<TarZstdFernet ' + s[1:-1] + ' ' + hex(id(self)) + '>'

def open(filename, mode="rb", fernet_key=None,
        chunk_size=CHUNK_SIZE,
        level_or_option=None, zstd_dict=None,
        **cryptor_args):
    """Open a ZstdFernet file in binary or text mode.

    The filename argument can be an actual filename (a str or bytes object), or
    an existing file object to read from or write to.

    The mode argument can be "r", "rb", "w", "wb", "x", "xb", "a" or "ab" for
    binary mode.

    """
    return _open_cls(filename, mode=mode,
        chunk_size=chunk_size, fernet_key=fernet_key,
        coffer_cls = TarFile,
        level_or_option=level_or_option, zstd_dict=zstd_dict,
        cryptor='fernet', **cryptor_args)
