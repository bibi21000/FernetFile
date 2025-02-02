# -*- encoding: utf-8 -*-
"""Test module

"""
import os
from random import randbytes
import tarfile
import bz2
import struct

from cryptography.fernet import Fernet

import fernetfile

import pytest

try:
    import pyzstd
    ZSTD = True
    class ZstdFernetFile(pyzstd.ZstdFile):

        def __init__(self, name, mode='r', fernet_key=None, chunk_size=fernetfile.CHUNK_SIZE, **kwargs):
            level_or_option = kwargs.pop('level_or_option', None)
            zstd_dict = kwargs.pop('zstd_dict', None)
            self.fernet_file = fernetfile.FernetFile(name, mode,
                fernet_key=fernet_key, chunk_size=chunk_size, **kwargs)
            try:
                super().__init__(self.fernet_file, mode=mode,
                    level_or_option=level_or_option,
                    zstd_dict=zstd_dict, **kwargs)
            except Exception:
                self.fernet_file.close()
                raise

        def close(self):
            try:
                super().close()
            finally:
                if self.fernet_file is not None:
                    self.fernet_file.close()

except ModuleNotFoundError:
    ZSTD = False
    # ~ class ZstdFernetFile():
        # ~ pass

class Bz2FernetFile(bz2.BZ2File):

    def __init__(self, name, mode='r', fernet_key=None, chunk_size=fernetfile.CHUNK_SIZE, **kwargs):
        compresslevel = kwargs.pop('compresslevel', 9)
        self.fernet_file = fernetfile.FernetFile(name, mode,
            fernet_key=fernet_key, chunk_size=chunk_size, **kwargs)
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

    def __init__(self, name, mode='r', fernet_key=None, chunk_size=fernetfile.CHUNK_SIZE, **kwargs):
        compresslevel = kwargs.pop('compresslevel', 9)

        self.bz2_file = bz2.BZ2File(name, mode,
            compresslevel=compresslevel, **kwargs)
        try:
            super().__init__(fileobj=self.bz2_file, mode=mode,
                fernet_key=fernet_key, chunk_size=chunk_size, **kwargs)
        except Exception:
            self.bz2_file.close()
            raise

    def close(self):
        try:
            super().close()
        finally:
            if self.bz2_file is not None:
                self.bz2_file.close()


class TarBz2FernetFile(tarfile.TarFile):

    def __init__(self, name, mode='r', fernet_key=None, chunk_size=fernetfile.CHUNK_SIZE, **kwargs):
        compresslevel = kwargs.pop('compresslevel', 9)
        self.fernet_file = fernetfile.FernetFile(name, mode,
            fernet_key=fernet_key, chunk_size=chunk_size, **kwargs)
        try:
            self.bz2_file = bz2.BZ2File(self.fernet_file, mode=mode,
                compresslevel=compresslevel, **kwargs)
            try:
                super().__init__(fileobj=self.bz2_file, mode=mode, **kwargs)

            except Exception:
                self.bz2_file.close()
                raise

        except Exception:
            self.fernet_file.close()
            raise

    def close(self):
        try:
            super().close()
        finally:
            try:
                if self.fernet_file is not None:
                    self.bz2_file.close()
            finally:
                if self.fernet_file is not None:
                    self.fernet_file.close()


@pytest.mark.parametrize("buff_size, file_size", [ (1024 * 10, 1024 * 1024 * 2) ])
def test_crypt_bz2(random_path, buff_size, file_size):
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


@pytest.mark.parametrize("buff_size, file_size", [ (1024 * 10, 1024 * 1024 * 2) ])
def test_bz2_crypt(random_path, buff_size, file_size):
    key = Fernet.generate_key()
    fkey = Fernet(key)
    data = randbytes(file_size)
    dataf = os.path.join(random_path, 'test.frnt')
    with FernetBz2File(dataf, mode='wb', fernet_key=key, chunk_size=buff_size) as ff:
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


@pytest.mark.skipif(not ZSTD, reason="requires the pyzstd library")
@pytest.mark.parametrize("buff_size, file_size", [ (1024 * 10, 1024 * 1024 * 2) ])
def test_crypt_zstd(random_path, buff_size, file_size):
    key = Fernet.generate_key()
    data = randbytes(file_size)
    dataf = os.path.join(random_path, 'test.frnt')
    with ZstdFernetFile(dataf, mode='wb', fernet_key=key, chunk_size=buff_size) as ff:
        ff.write(data)
    with open(dataf, "rb") as ff:
        datar = ff.read()
    assert data != datar
    with fernetfile.open(dataf, "rb", fernet_key=key) as ff:
        datar = ff.read()
        datar = pyzstd.decompress(datar)
    assert data == datar
    with ZstdFernetFile(dataf, "rb", fernet_key=key) as ff:
        datar = ff.read()
    assert data == datar


@pytest.mark.parametrize("buff_size, file_size", [ (1024 * 10, 1024 * 1024 * 2) ])
def test_crypt_bz2_tar(random_path, buff_size, file_size):
    key = Fernet.generate_key()
    dataf = os.path.join(random_path, 'test.tbzf')

    dataf1 = os.path.join(random_path, 'file1.out')
    with open(dataf1, "wb") as out:
        out.write(os.urandom(file_size * 5))
    with open(dataf1, "rb") as ff:
        ddataf1 = ff.read()

    dataf2 = os.path.join(random_path, 'file2.out')
    with open(dataf2, "wb") as out:
        out.write(os.urandom(file_size * 50))
    with open(dataf2, "rb") as ff:
        ddataf2 = ff.read()

    with TarBz2FernetFile(dataf, mode='w', fernet_key=key, chunk_size=buff_size) as ff:
        ff.add(dataf1, 'file1.out')
        ff.add(dataf2, 'file2.out')

    os.unlink(dataf1)
    os.unlink(dataf2)

    with TarBz2FernetFile(dataf, "r", fernet_key=key) as ff:
        fdatae = ff.extractfile('file1.out')
        assert fdatae.read() == ddataf1
        fdatae = ff.extractfile('file2.out')
        assert fdatae.read() == ddataf2

