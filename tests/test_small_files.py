# -*- encoding: utf-8 -*-
"""Test module

"""
import os
import importlib
import time
from random import randbytes
import urllib.request
import zipfile
import tarfile

from cryptography.fernet import Fernet, InvalidToken

import fernetfile
from fernetfile import FernetFile
from fernetfile.zstd import FernetFile as _ZstdFernetFile, open as fernetz_open
from fernetfile.tar import TarFile as _TarZstdFernetFile

import pytest


class ZstdFernetFile(_ZstdFernetFile):
    pass

class TarZstdFernetFile(_TarZstdFernetFile):
    pass

@pytest.mark.parametrize("fcls, size, nb", [
    (TarZstdFernetFile, 129, 100),
    (TarZstdFernetFile, 533, 20),
    (TarZstdFernetFile, 1089, 5),
])
def test_benchmark_tar(random_path, fcls, size, nb):
    if os.path.isfile('docpython.pdf.zip') is False:
        urllib.request.urlretrieve("https://docs.python.org/3/archives/python-3.13-docs-pdf-a4.zip", "docpython.pdf.zip")
        with zipfile.ZipFile('docpython.pdf.zip', 'r') as zip_ref:
            zip_ref.extractall('.')
    if os.path.isfile('docpython.html.zip') is False:
        urllib.request.urlretrieve("https://docs.python.org/3/archives/python-3.13-docs-html.zip", "docpython.html.zip")
        with zipfile.ZipFile('docpython.html.zip', 'r') as zip_ref:
            zip_ref.extractall('.')
    params = {
        'fernet_key': Fernet.generate_key(),
    }
    dataf = os.path.join(random_path, 'test.frnt')
    time_start = time.time()
    file_size = 0
    data1f = os.path.join(random_path, 'file.data')
    data1 = randbytes(size)
    with open(data1f, 'wb') as ff:
        ff.write(data1)
    with fcls(dataf, mode='w', **params) as ff:
        for i in range(nb):
            ff.add(data1f, "%s-%s"%(i, data1f))
            file_size += os.path.getsize(data1f)
    time_write = time.time()
    with fcls(dataf, "r", **params) as ff:
        ff.extractall('extract_tar')
    time_read = time.time()
    # ~ assert data == datar
    comp_size = os.path.getsize(dataf)
    for i in range(nb):
        with open(os.path.join('extract_tar', "%s-%s"%(i, data1f)),'rb') as ff:
            data1r = ff.read()
            assert data1 == data1r

