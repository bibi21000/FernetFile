# -*- encoding: utf-8 -*-
"""Test module

"""
import os
from random import randbytes
import io

from cryptography.fernet import Fernet

import fernetfile

import pytest

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
    with fernetfile.open(dataf, mode='wb', fernet_key=key) as ff:
        ff.write(data)
    with open(dataf, "rb") as ff:
        datar = ff.read()
    assert data != datar
    with fernetfile.open(dataf, "rb", fernet_key=key) as ff:
        datar = ff.read()
    fernetfile.BUFFER_SIZE = 1024 * 10
    assert data == datar

def test_encoding(random_path):
    key = Fernet.generate_key()
    datal = ["Ceci est un texte avec des accents : éè","avec plusieurs","lignes"]
    data = "\n".join(datal)
    dataf = os.path.join(random_path, 'test_encoding.frnt')

    with fernetfile.open(dataf, mode='wt', fernet_key=key, encoding="utf-8") as ff:
        ff.write(data)

    with pytest.raises(ValueError):
        with open(dataf, "r", encoding="utf-8") as ff:
            datar = ff.read()
        assert data != datar

    with fernetfile.open(dataf, "rt", fernet_key=key, encoding="utf-8") as ff:
        datar = ff.read()
    assert data == datar

    with fernetfile.open(dataf, "rt", fernet_key=key, encoding="utf-8") as ff:
        datar = ff.read()
    assert data == datar

    with fernetfile.open(dataf, "rt", fernet_key=key, encoding="utf-8") as ff:
        datar = ff.readline()
        assert datal[0] + '\n' == datar
        datar = ff.readline()
        assert datal[1] + '\n' == datar
        datar = ff.readline()
        assert datal[2] == datar

def test_seek(random_path):
    key = Fernet.generate_key()
    data = randbytes(1784) + b'0111110' + randbytes(3594) + b'0100010' + randbytes(2145)
    dataf = os.path.join(random_path, 'test_seek.frnt')

    with fernetfile.open(dataf, mode='wb', fernet_key=key) as ff:
        assert ff.fileno() is not None
        ff.write(data)
        assert ff.writable()
        assert not ff.readable()
        with pytest.raises(OSError):
            ff.rewind()
        with pytest.raises(OSError):
            ff.seek(0, whence=io.SEEK_SET)
        ff.seek(0, whence=io.SEEK_CUR)

    with fernetfile.open(dataf, "rb", fernet_key=key) as ff:
        assert ff.fileno() is not None
        assert ff.readable()
        assert not ff.writable()
        datar = ff.read()
        assert data == datar
        ff.rewind()
        # ~ assert ff.offset == 0
        datar = ff.read()
        assert data == datar
        ff.seek(1784, whence=io.SEEK_SET)
        datar = ff.read(size=7)
        assert b'0111110' == datar[:7]
        ff.seek(3594, whence=io.SEEK_CUR)
        datar = ff.read()
        assert b'0100010' == datar[:7]

    with open(dataf, "rb") as fp:
        with fernetfile.open(fp, "rb", fernet_key=key) as ff:
            datar = ff.read()
            assert data == datar
            ff.rewind()
            # ~ assert ff.offset == 0
            datar = ff.read()
            assert data == datar
            ff.seek(1784, whence=io.SEEK_SET)
            datar = ff.read(size=7)
            assert b'0111110' == datar[:7]

    with fernetfile.open(dataf, "rb", fernet_key=key) as ff:
        ff.seek(-(2145+7), whence=io.SEEK_END)
        datar = ff.read(7)
        assert b'0100010' == datar

def test_reader(random_path):
    key = Fernet.generate_key()
    data = randbytes(1784) + b'0111110' + randbytes(3594) + b'0100010' + randbytes(2145)
    dataf = os.path.join(random_path, 'test_reader.frnt')

    with fernetfile.open(dataf, mode='wb', fernet_key=key) as ff:
        assert ff.fileno() is not None
        ff.write(data)
        assert ff.writable()
        assert not ff.readable()
        with pytest.raises(OSError):
            ff.rewind()
        with pytest.raises(ValueError):
            ff.seek(-1, whence=io.SEEK_END)
        with pytest.raises(OSError):
            ff.seek(-1)

    with open(dataf, "rb") as ff:
        with fernetfile.DecryptReader(ff, fernetfile.FernetDecryptor, fernet_key=key) as fp:
            assert fp.readable()
            assert not fp.writable()
            datar = fp.read()
            assert data == datar
            fp.rewind()
            datar = fp.read(1784)
            datar = fp.read(7)
            assert b'0111110' == datar
            fp.seek(-7, whence=io.SEEK_CUR)
            datar = fp.read(7)
            assert b'0111110' == datar
            fp.seek(-7, whence=io.SEEK_CUR)
            assert fp.tell() == 1784
            datar = fp.read(7)
            assert b'0111110' == datar
            fp.seek(0, whence=io.SEEK_END)
            fp.seek(-(2145+7), whence=io.SEEK_END)
            datar = fp.read(7)
            assert b'0100010' == datar
            with pytest.raises(ValueError):
                fp.seek(0, 999999)

def test_bad_mode(random_path):
    key = Fernet.generate_key()
    data = randbytes(128)
    dataf = os.path.join(random_path, 'test_bad_mode.frnt')

    with pytest.raises(ValueError):
        with fernetfile.FernetFile(dataf, mode='wbt', fernet_key=key) as ff:
            ff.write(data)

    with pytest.raises(ValueError):
        with fernetfile.FernetFile(dataf, mode='zzz', fernet_key=key) as ff:
            ff.write(data)

    with pytest.raises(FileNotFoundError):
        with fernetfile.FernetFile(None, mode='wb', fernet_key=key) as ff:
            ff.write(data)

    with pytest.raises(FileNotFoundError):
        with fernetfile.FernetFile(dataf, fernet_key=key) as ff:
            data = ff.read()

    with pytest.raises(ValueError):
        with fernetfile.open(dataf, mode='wbt', fernet_key=key) as ff:
            ff.write(data)

    with pytest.raises(ValueError):
        with fernetfile.open(dataf, mode='wb', fernet_key=key, encoding='utf-8') as ff:
            ff.write(data)

    with pytest.raises(ValueError):
        with fernetfile.open(dataf, mode='wb', fernet_key=key, errors=True) as ff:
            ff.write(data)

    with pytest.raises(ValueError):
        with fernetfile.open(dataf, mode='wb', fernet_key=key, newline='\n') as ff:
            ff.write(data)

    with pytest.raises(TypeError):
        with fernetfile.open(None, mode='wb', fernet_key=key) as ff:
            ff.write(data)

def test_fernetfile(random_path):
    key = Fernet.generate_key()
    data = randbytes(128)
    dataf = os.path.join(random_path, 'test_repr.frnt')
    with fernetfile.FernetFile(dataf, mode='wb', fernet_key=key) as ff:
        ff.write(data)
        assert ff.seekable() is False
        assert repr(ff).startswith("<FernetFile ")
        with pytest.raises(OSError):
            data = ff.read()
        with pytest.raises(OSError):
            data = ff.read1()
        with pytest.raises(OSError):
            data = ff.peek(1)
        ff.fileobj = None
        with pytest.raises(ValueError):
            ff.write(b'rrrrrrrr')
        with pytest.raises(ValueError):
            ff.seekable()

    with fernetfile.FernetFile(dataf, mode='wb', fernet_key=key) as ff:
        ff.write(data)

    with fernetfile.FernetFile(dataf, mode='rb', fernet_key=key) as ff:
        fpp = ff
        with pytest.raises(OSError):
            ff.write(b'rrrrrrrr')
        ff.seek(-1)
        assert ff.tell() == 0
        assert ff.seekable() is True

    with fernetfile.FernetFile(dataf, mode='rb', fernet_key=key) as ff:
        fpp = ff
        with pytest.raises(OSError):
            ff.write(b'rrrrrrrr')
        ff.seek(-1)

    with pytest.raises(ValueError):
        fpp.write(b'rrrrrrrr')
    fpp.close()

    with pytest.raises(ValueError):
        with fernetfile.FernetFile(dataf, mode='fff', fileobj="fake", fernet_key=key) as ff:
            data = ff.read()

def test_peek(random_path):
    key = Fernet.generate_key()
    data = b'azazazazazazaz\n'
    dataf = os.path.join(random_path, 'test_repr.frnt')
    with fernetfile.FernetFile(dataf, mode='wb', fernet_key=key) as ff:
        ff.write(data)

    with fernetfile.FernetFile(dataf, mode='wb', fernet_key=key) as ff:
        ff.write(data)

    with fernetfile.FernetFile(dataf, mode='rb', fernet_key=key) as ff:
        datar = ff.read1()
        assert datar == data

    with fernetfile.FernetFile(dataf, mode='rb', fernet_key=key) as ff:
        datar = ff.read1(1)
        assert datar == b'a'

    with fernetfile.FernetFile(dataf, mode='rb', fernet_key=key) as ff:
        datar = ff.readline()
        assert datar == data

    with fernetfile.FernetFile(dataf, mode='rb', fernet_key=key) as ff:
        data = ff.peek(128)
        assert datar == data

