# -*- encoding: utf-8 -*-
"""Test module

"""
import os
from random import randbytes
import io
import bz2
import struct

from cryptography.fernet import Fernet

import fernetfile

import pytest


class Bz2FernetFile(bz2.BZ2File):

    def __init__(self, name, mode='r', fernet_key=None, **kwargs):
        compresslevel = kwargs.pop('compresslevel', 9)
        self.fernet_file = fernetfile.FernetFile(name, mode,
            fernet_key=fernet_key, **kwargs)
        try:
            super().__init__(self.fernet_file, mode=mode,
                compresslevel=compresslevel, **kwargs)
        except Exception:
            self.fernet_file.close()
            raise

    def close(self):
        try:
            super().close()
        finally:
            if self.fernet_file is not None:
                self.fernet_file.close()


class FernetBz2File(fernetfile.FernetFile):

    def __init__(self, name, mode='r', fernet_key=None, **kwargs):
        compresslevel = kwargs.pop('compresslevel', 9)

        self.bz2_file = bz2.BZ2File(name, mode,
            compresslevel=compresslevel, **kwargs)
        try:
            super().__init__(fileobj=self.bz2_file, mode=mode,
                fernet_key=fernet_key, **kwargs)
        except Exception:
            self.bz2_file.close()
            raise

    def close(self):
        try:
            super().close()
        finally:
            if self.bz2_file is not None:
                self.bz2_file.close()


@pytest.mark.parametrize("buff_size, file_size", [ (1024 * 1, 1024 * 1024 * 10) ])
def test_crypt_compress(random_path, buff_size, file_size):
    key = Fernet.generate_key()
    data = randbytes(file_size)
    dataf = os.path.join(random_path, 'test.frnt')
    with Bz2FernetFile(dataf, mode='wb', fernet_key=key) as ff:
        ff.write(data)
    with open(dataf, "rb") as ff:
        datar = ff.read()
    assert data != datar
    with fernetfile.open(dataf, "rb", fernet_key=key) as ff:
        datar = ff.read()
        datar = bz2.decompress(datar)
    assert data == datar
    with Bz2FernetFile(dataf, "rb", fernet_key=key) as ff:
        datar = ff.read()
    assert data == datar


@pytest.mark.parametrize("buff_size, file_size", [ (1024 * 1, 1024 * 1024 * 10) ])
def test_compress_crypt(random_path, buff_size, file_size):
    key = Fernet.generate_key()
    fkey = Fernet(key)
    data = randbytes(file_size)
    dataf = os.path.join(random_path, 'test.frnt')
    with FernetBz2File(dataf, mode='wb', fernet_key=key) as ff:
        ff.write(data)
    with open(dataf, "rb") as ff:
        datar = ff.read()
    assert data != datar
    with bz2.open(dataf, "rb") as ff:
        datar = ff.read()
    beg = 0
    datau = b''
    while True:
        size_struct = datar[beg:beg + 4]
        if len(size_struct) == 0:
            break
        size_data = struct.unpack('<I', size_struct)[0]
        chunk = datar[beg + 4:beg + size_data + 4]
        beg += size_data + 4
        datau += fkey.decrypt(chunk)
    assert data == datau
    with FernetBz2File(dataf, "rb", fernet_key=key) as ff:
        datar = ff.read()
    assert data == datar

