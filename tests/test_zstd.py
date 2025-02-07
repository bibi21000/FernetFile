# -*- encoding: utf-8 -*-
"""Test module

"""
import os
import io
from random import randbytes
import tarfile
import lzma
import bz2
import zipfile
import struct

from cryptography.fernet import Fernet

import fernetfile

import pytest


try:
    import pyzstd
    ZSTD = True

    from fernetfile.zstd import FernetFile as ZstdFernetFile, open as zstd_open

    class TarZstdFernetFile(tarfile.TarFile):

        def __init__(self, name, mode='r', fernet_key=None, chunk_size=fernetfile.CHUNK_SIZE, **kwargs):
            level_or_option = kwargs.pop('level_or_option', None)
            zstd_dict = kwargs.pop('zstd_dict', None)
            self.fernet_file = fernetfile.FernetFile(name, mode,
                fernet_key=fernet_key, chunk_size=chunk_size, **kwargs)
            try:
                self.zstd_file = pyzstd.ZstdFile(self.fernet_file, mode=mode,
                    level_or_option=level_or_option, zstd_dict=zstd_dict, **kwargs)
                try:
                    super().__init__(fileobj=self.zstd_file, mode=mode, **kwargs)

                except Exception:
                    self.zstd_file.close()
                    raise

            except Exception:
                self.fernet_file.close()
                raise

        def close(self):
            try:
                super().close()
            finally:
                try:
                    if self.zstd_file is not None:
                        self.zstd_file.close()
                finally:
                    if self.fernet_file is not None:
                        self.fernet_file.close()

except ModuleNotFoundError:
    ZSTD = False
    # ~ class ZstdFernetFile():
        # ~ pass

@pytest.mark.skipif(not ZSTD, reason="requires the pyzstd library")
@pytest.mark.parametrize("buff_size, file_size", [ (1024 * 32, 1024 * 1024 * 1) ])
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


@pytest.mark.skipif(not ZSTD, reason="requires the pyzstd library")
@pytest.mark.parametrize("buff_size, file_size", [ (1024 * 64, 1024 * 512 + 21) ])
def test_crypt_zstd_tar(random_path, buff_size, file_size):
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

    with TarZstdFernetFile(dataf, mode='w', fernet_key=key, chunk_size=buff_size) as ff:
        ff.add(dataf1, 'file1.out')
        ff.add(dataf2, 'file2.out')

    os.unlink(dataf1)
    os.unlink(dataf2)

    with TarZstdFernetFile(dataf, "r", fernet_key=key) as ff:
        fdatae = ff.extractfile('file1.out')
        assert fdatae.read() == ddataf1
        fdatae = ff.extractfile('file2.out')
        assert fdatae.read() == ddataf2

@pytest.mark.parametrize("buff_size, file_size", [ (1024 * 32, 1024 * 512 + 31) ])
def test_crypt_zstd_tar_append(random_path, buff_size, file_size):
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

    dataf3 = os.path.join(random_path, 'file3.out')
    with open(dataf3, "wb") as out:
        out.write(os.urandom(file_size * 10))
    with open(dataf3, "rb") as ff:
        ddataf3 = ff.read()

    with TarZstdFernetFile(dataf, mode='w', fernet_key=key, chunk_size=buff_size) as ff:
        ff.add(dataf1, 'file1.out')
        ff.add(dataf2, 'file2.out')

    os.unlink(dataf1)
    os.unlink(dataf2)

    # Can't append to tar/bz2
    with pytest.raises(io.UnsupportedOperation):
        with TarZstdFernetFile(dataf, mode='a', fernet_key=key, chunk_size=buff_size) as ff:
            ff.add(dataf3, 'file3.out')

    # ~ os.unlink(dataf3)

    # ~ with TarZstdFernetFile(dataf, "r", fernet_key=key) as ff:
        # ~ fdatae = ff.extractfile('file1.out')
        # ~ assert fdatae.read() == ddataf1
        # ~ fdatae = ff.extractfile('file2.out')
        # ~ assert fdatae.read() == ddataf2
        # ~ fdatae = ff.extractfile('file3.out')
        # ~ assert fdatae.read() == ddataf3

def test_zstd_encoding(random_path):
    key = Fernet.generate_key()
    datal = ["Ceci est un texte avec des accents : éè","avec plusieurs","lignes"]
    data = "\n".join(datal)
    dataf = os.path.join(random_path, 'test_encoding.frnt')

    with zstd_open(dataf, mode='wt', fernet_key=key, encoding="utf-8") as ff:
        ff.write(data)

    with pytest.raises(ValueError):
        with open(dataf, "r", encoding="utf-8") as ff:
            datar = ff.read()
        assert data != datar

    with zstd_open(dataf, "rt", fernet_key=key, encoding="utf-8") as ff:
        datar = ff.read()
    assert data == datar

    with zstd_open(dataf, "rt", fernet_key=key, encoding="utf-8") as ff:
        datar = ff.read()
    assert data == datar

    with zstd_open(dataf, "rt", fernet_key=key, encoding="utf-8") as ff:
        datar = ff.readline()
        assert datal[0] + '\n' == datar
        datar = ff.readline()
        assert datal[1] + '\n' == datar
        datar = ff.readline()
        assert datal[2] == datar

    datal = ["Ceci est un texte avec des accents : éè","avec plusieurs","lignes"]
    dataf = os.path.join(random_path, 'test_encoding.frnt')

    with zstd_open(dataf, mode='wt', fernet_key=key, encoding="utf-8") as ff:
        ff.writelines(data)

    with zstd_open(dataf, "rt", fernet_key=key, encoding="utf-8") as ff:
        datar = ff.readlines()

    assert datal[0] + '\n' == datar[0]
    assert datal[1] + '\n' == datar[1]
    assert datal[2] == datar[2]


def test_files_zstd_encrypt(random_path):

    key = Fernet.generate_key()

    datafsrc = os.path.join(random_path, 'test.dat')
    dataftgt = os.path.join(random_path, 'test.dtc')
    datafdec = os.path.join(random_path, 'test.dec')

    with open(datafsrc, 'wb') as f:
        for i in range(1024):
            f.write(randbytes(1024 * 5))

    with open(datafsrc, 'rb') as fin, zstd_open(dataftgt, mode='wb', fernet_key=key) as fout:
        while True:
            data = fin.read(7777)
            if not data:
                break
            fout.write(data)

    with zstd_open(dataftgt, mode='rb', fernet_key=key) as fin, open(datafdec, 'wb') as fout :
        while True:
            data = fin.read(8888)
            if not data:
                break
            fout.write(data)

    with open(datafsrc, 'rb') as f1, open(datafdec, 'rb') as f2:
        assert f1.read() == f2.read()

@pytest.mark.parametrize("buff_size, file_size",
    [
        (1024 * 1, 1024 * 10), (1024 * 1, 1024 * 10 + 4), (1024 * 1, 1024 * 10 + 5),
        (1024 * 10, 1024 * 10), (1024 * 10, 1024 * 10 + 7), (1024 * 10, 1024 * 10 + 3),
        (1024 * 100, 1024 * 10), (1024 * 100, 1024 * 10 + 9), (1024 * 100, 1024 * 10 + 11),
    ])
def test_buffer(random_path, buff_size, file_size):
    fernetfile.BUFFER_SIZE = buff_size
    key = Fernet.generate_key()
    data = randbytes(file_size)
    dataf = os.path.join(random_path, 'test.frnt')
    with zstd_open(dataf, mode='wb', fernet_key=key) as ff:
        ff.write(data)
    with open(dataf, "rb") as ff:
        datar = ff.read()
    assert data != datar
    with zstd_open(dataf, "rb", fernet_key=key) as ff:
        datar = ff.read()
    fernetfile.BUFFER_SIZE = 1024 * 10
    assert data == datar

def test_zst_bad_mode(random_path):
    key = Fernet.generate_key()
    data = randbytes(128)
    dataf = os.path.join(random_path, 'test_bad_mode.frnt')

    print(repr(ZstdFernetFile))

    with pytest.raises(ValueError):
        with ZstdFernetFile(dataf, mode='wbt', fernet_key=key) as ff:
            ff.write(data)

    with pytest.raises(ValueError):
        with ZstdFernetFile(dataf, mode='zzz', fernet_key=key) as ff:
            ff.write(data)

    with pytest.raises(FileNotFoundError):
        with ZstdFernetFile(None, mode='wb', fernet_key=key) as ff:
            ff.write(data)

    with pytest.raises(FileNotFoundError):
        with ZstdFernetFile(dataf, fernet_key=key) as ff:
            data = ff.read()

    with pytest.raises(ValueError):
        with zstd_open(dataf, mode='wbt', fernet_key=key) as ff:
            ff.write(data)

    with pytest.raises(ValueError):
        with zstd_open(dataf, mode='wb', fernet_key=key, encoding='utf-8') as ff:
            ff.write(data)

    with pytest.raises(ValueError):
        with zstd_open(dataf, mode='wb', fernet_key=key, errors=True) as ff:
            ff.write(data)

    with pytest.raises(ValueError):
        with zstd_open(dataf, mode='wb', fernet_key=key, newline='\n') as ff:
            ff.write(data)

    with pytest.raises(TypeError):
        with zstd_open(None, mode='wb', fernet_key=key) as ff:
            ff.write(data)

    with pytest.raises(ValueError):
        with zstd_open(dataf, mode='wb', fernet_key=None) as ff:
            ff.write(data)
