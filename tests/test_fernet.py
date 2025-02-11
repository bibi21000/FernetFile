# -*- encoding: utf-8 -*-
"""Test module

"""
import os
import io
from random import randbytes
import tarfile
import struct

from cryptography.fernet import Fernet, InvalidToken

import cofferfile
from fernetfile import FernetFile, open as fernet_open

import pytest

@pytest.mark.parametrize("chunk_size, file_size",
    [
        (1024 * 1, 1024 * 10), (1024 * 1, 1024 * 10 + 4), (1024 * 1, 1024 * 10 + 5),
        (1024 * 10, 1024 * 10), (1024 * 10, 1024 * 10 + 7), (1024 * 10, 1024 * 10 + 3),
        (1024 * 100, 1024 * 10), (1024 * 100, 1024 * 10 + 9), (1024 * 100, 1024 * 10 + 11),
    ])
def test_buffer_fernet_file(random_path, random_name, chunk_size, file_size):

    key = Fernet.generate_key()

    data = randbytes(file_size)
    dataf = os.path.join(random_path, random_name)
    with FernetFile(dataf, mode='wb', fernet_key=key, chunk_size=chunk_size) as ff:
        ff.write(data)
    with open(dataf, "rb") as ff:
        datar = ff.read()
    assert data != datar
    with FernetFile(dataf, "rb", fernet_key=key) as ff:
        datar = ff.read()
    assert data == datar

    data = random_name * 2
    dataf = os.path.join(random_path, random_name)
    with fernet_open(dataf, mode='wt', fernet_key=key, chunk_size=chunk_size) as ff:
        ff.write(data)
    with open(dataf, "rb") as ff:
        datar = ff.read()
    assert data != datar
    with fernet_open(dataf, "rt", fernet_key=key) as ff:
        datar = ff.read()
    assert data == datar

@pytest.mark.parametrize("chunk_size, file_size",
    [
        (1024 * 1, 1024 * 10), (1024 * 1, 1024 * 10 + 4), (1024 * 1, 1024 * 10 + 5),
        (1024 * 10, 1024 * 10), (1024 * 10, 1024 * 10 + 7), (1024 * 10, 1024 * 10 + 3),
        (1024 * 100, 1024 * 10), (1024 * 100, 1024 * 10 + 9), (1024 * 100, 1024 * 10 + 11),
    ])
def test_buffer_fernet_open(random_path, random_name, chunk_size, file_size):

    key = Fernet.generate_key()

    data = randbytes(file_size)
    dataf = os.path.join(random_path, random_name)
    with fernet_open(dataf, mode='wb', fernet_key=key, chunk_size=chunk_size) as ff:
        ff.write(data)
    with open(dataf, "rb") as ff:
        datar = ff.read()
    assert data != datar
    with fernet_open(dataf, "rb", fernet_key=key) as ff:
        datar = ff.read()
    assert data == datar

    data = random_name * 2
    dataf = os.path.join(random_path, random_name)
    with fernet_open(dataf, mode='wt', fernet_key=key, chunk_size=chunk_size) as ff:
        ff.write(data)
    with open(dataf, "rb") as ff:
        datar = ff.read()
    assert data != datar
    with fernet_open(dataf, "rt", fernet_key=key) as ff:
        datar = ff.read()
    assert data == datar

def test_bad(random_path, random_name):
    key = Fernet.generate_key()
    data = randbytes(128)
    dataf = os.path.join(random_path, 'test_bad_%s.frnt'%random_name)
    dataok = os.path.join(random_path, 'test_ok_%s.frnt'%random_name)

    with FernetFile(dataok, mode='wb', fernet_key=key) as ff:
        assert repr(ff).startswith('<FernetFile')

    with pytest.raises(ValueError):
        with FernetFile(dataf, mode='wbt', fernet_key=key) as ff:
            ff.write(data)

    with pytest.raises(ValueError):
        with FernetFile(dataf, mode='zzz', fernet_key=key) as ff:
            ff.write(data)

    with pytest.raises(FileNotFoundError):
        with FernetFile(None, mode='wb', fernet_key=key) as ff:
            ff.write(data)

    with pytest.raises(FileNotFoundError):
        with FernetFile(dataf, fernet_key=key) as ff:
            data = ff.read()

    with pytest.raises(ValueError):
        with fernet_open(dataf, mode='wbt', fernet_key=key) as ff:
            ff.write(data)

    with pytest.raises(ValueError):
        with fernet_open(dataf, mode='wb', fernet_key=key, encoding='utf-8') as ff:
            ff.write(data)

    with pytest.raises(ValueError):
        with fernet_open(dataf, mode='wb', fernet_key=key, errors=True) as ff:
            ff.write(data)

    with pytest.raises(ValueError):
        with fernet_open(dataf, mode='wb', fernet_key=key, newline='\n') as ff:
            ff.write(data)

    with pytest.raises(TypeError):
        with fernet_open(None, mode='wb', fernet_key=key) as ff:
            ff.write(data)

    with pytest.raises(ValueError):
        with fernet_open(dataf, mode='wb', fernet_key=None) as ff:
            ff.write(data)
