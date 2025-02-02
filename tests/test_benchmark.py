# -*- encoding: utf-8 -*-
"""Test module

"""
import os
import importlib
import time
from random import randbytes
import bz2
import urllib.request
import zipfile

from cryptography.fernet import Fernet

import fernetfile

import pytest
from .test_chain import Bz2FernetFile, ZstdFernetFile, TarBz2FernetFile, TarZstdFernetFile

# ~ @pytest.mark.skip("Manual test")
@pytest.mark.skipif(not importlib.util.find_spec("pytest_ordering"), reason="requires the pytest_ordering package")
@pytest.mark.run(order=1)
def test_benchmark_header(random_path):
    with open('BENCHMARK.md','wt') as ff:
        ff.write("# Benchmarks\n")
        ff.write("\n")
        ff.write("| Class                | Data                 |  Chunk size |  Orig size  | Crypt size |  Comp ratio | WTime  | Rtime  |\n")
        ff.write("|:---------------------|:---------------------|------------:|------------:|-----------:|------------:|-------:|-------:|\n")
    urllib.request.urlretrieve("https://docs.python.org/3/archives/python-3.13-docs-pdf-a4.zip", "docpython.pdf.zip")
    with zipfile.ZipFile('docpython.pdf.zip', 'r') as zip_ref:
        zip_ref.extractall('.')
    urllib.request.urlretrieve("https://docs.python.org/3/archives/python-3.13-docs-html.zip", "docpython.html.zip")
    with zipfile.ZipFile('docpython.html.zip', 'r') as zip_ref:
        zip_ref.extractall('.')

# ~ @pytest.mark.skip("Manual test")
@pytest.mark.skipif(not importlib.util.find_spec("pytest_ordering"), reason="requires the pytest_ordering package")
@pytest.mark.run(order=2)
@pytest.mark.parametrize("fcls, dt, buff_size, file_size", [
    (fernetfile.FernetFile, 'download.html', 1024 * 16, 0),
    (fernetfile.FernetFile, 'genindex-all.html', 1024 * 16, 0),
    (fernetfile.FernetFile, 'searchindex.js', 1024 * 16, 0),
    (fernetfile.FernetFile, 'library.pdf', 1024 * 16, 0),
    # ~ (fernetfile.FernetFile, 'rand', 1024 * 16, 1024 * 1024 * 1),
    # ~ (fernetfile.FernetFile, 'rand', 1024 * 16, 1024 * 1024 * 10),
    # ~ (fernetfile.FernetFile, 'rand', 1024 * 16, 1024 * 1024 * 100),
    (Bz2FernetFile, 'download.html', 1024 * 16, 0),
    (Bz2FernetFile, 'genindex-all.html', 1024 * 16, 0),
    (Bz2FernetFile, 'searchindex.js', 1024 * 16, 0),
    (Bz2FernetFile, 'library.pdf', 1024 * 16, 0),
    # ~ (Bz2FernetFile, 'rand', 1024 * 16, 1024 * 1024 * 1),
    # ~ (Bz2FernetFile, 'rand', 1024 * 16, 1024 * 1024 * 10),
    # ~ (Bz2FernetFile, 'rand', 1024 * 16, 1024 * 1024 * 100),
    (ZstdFernetFile, 'download.html', 1024 * 16, 0),
    (ZstdFernetFile, 'genindex-all.html', 1024 * 16, 0),
    (ZstdFernetFile, 'searchindex.js', 1024 * 16, 0),
    (ZstdFernetFile, 'library.pdf', 1024 * 16, 0),
    # ~ (ZstdFernetFile, 'rand', 1024 * 16, 1024 * 1024 * 1),
    # ~ (ZstdFernetFile, 'rand', 1024 * 16, 1024 * 1024 * 10),
    # ~ (ZstdFernetFile, 'rand', 1024 * 16, 1024 * 1024 * 100),
    # ~ (fernetfile.FernetFile, b'a', 1024 * 16, 1024 * 1024 * 1),
    # ~ (fernetfile.FernetFile, b'b', 1024 * 16, 1024 * 1024 * 10),
    # ~ (fernetfile.FernetFile, b'c', 1024 * 16, 1024 * 1024 * 100),
    # ~ (Bz2FernetFile, b'd', 1024 * 16, 1024 * 1024 * 1),
    # ~ (Bz2FernetFile, b'e', 1024 * 16, 1024 * 1024 * 10),
    # ~ (Bz2FernetFile, b'f', 1024 * 16, 1024 * 1024 * 100),
    # ~ (ZstdFernetFile, b'g', 1024 * 16, 1024 * 1024 * 1),
    # ~ (ZstdFernetFile, b'h', 1024 * 16, 1024 * 1024 * 10),
    # ~ (ZstdFernetFile, b'i', 1024 * 16, 1024 * 1024 * 100),
    (fernetfile.FernetFile, 'download.html', 1024 * 256, 0),
    (fernetfile.FernetFile, 'genindex-all.html', 1024 * 256, 0),
    (fernetfile.FernetFile, 'searchindex.js', 1024 * 256, 0),
    (fernetfile.FernetFile, 'library.pdf', 1024 * 256, 0),
    # ~ (fernetfile.FernetFile, 'rand', 1024 * 256, 1024 * 1024 * 1),
    # ~ (fernetfile.FernetFile, 'rand', 1024 * 256, 1024 * 1024 * 10),
    # ~ (fernetfile.FernetFile, 'rand', 1024 * 256, 1024 * 1024 * 100),
    (Bz2FernetFile, 'download.html', 1024 * 256, 0),
    (Bz2FernetFile, 'genindex-all.html', 1024 * 256, 0),
    (Bz2FernetFile, 'searchindex.js', 1024 * 256, 0),
    (Bz2FernetFile, 'library.pdf', 1024 * 256, 0),
    # ~ (Bz2FernetFile, 'rand', 1024 * 256, 1024 * 1024 * 1),
    # ~ (Bz2FernetFile, 'rand', 1024 * 256, 1024 * 1024 * 10),
    # ~ (Bz2FernetFile, 'rand', 1024 * 256, 1024 * 1024 * 100),
    (ZstdFernetFile, 'download.html', 1024 * 256, 0),
    (ZstdFernetFile, 'genindex-all.html', 1024 * 256, 0),
    (ZstdFernetFile, 'searchindex.js', 1024 * 256, 0),
    (ZstdFernetFile, 'library.pdf', 1024 * 256, 0),
    # ~ (ZstdFernetFile, 'rand', 1024 * 256, 1024 * 1024 * 1),
    # ~ (ZstdFernetFile, 'rand', 1024 * 256, 1024 * 1024 * 10),
    # ~ (ZstdFernetFile, 'rand', 1024 * 256, 1024 * 1024 * 100),
    # ~ (fernetfile.FernetFile, b'a', 1024 * 256, 1024 * 1024 * 1),
    # ~ (fernetfile.FernetFile, b'b', 1024 * 256, 1024 * 1024 * 10),
    # ~ (fernetfile.FernetFile, b'c', 1024 * 256, 1024 * 1024 * 100),
    # ~ (Bz2FernetFile, b'd', 1024 * 256, 1024 * 1024 * 1),
    # ~ (Bz2FernetFile, b'e', 1024 * 256, 1024 * 1024 * 10),
    # ~ (Bz2FernetFile, b'f', 1024 * 256, 1024 * 1024 * 100),
    # ~ (ZstdFernetFile, b'g', 1024 * 256, 1024 * 1024 * 1),
    # ~ (ZstdFernetFile, b'h', 1024 * 256, 1024 * 1024 * 10),
    # ~ (ZstdFernetFile, b'i', 1024 * 256, 1024 * 1024 * 100),
    (fernetfile.FernetFile, 'download.html', 1024 * 1024, 0),
    (fernetfile.FernetFile, 'genindex-all.html', 1024 * 1024, 0),
    (fernetfile.FernetFile, 'searchindex.js', 1024 * 1024, 0),
    (fernetfile.FernetFile, 'library.pdf', 1024 * 1024, 0),
    (Bz2FernetFile, 'download.html', 1024 * 1024, 0),
    (Bz2FernetFile, 'genindex-all.html', 1024 * 1024, 0),
    (Bz2FernetFile, 'searchindex.js', 1024 * 1024, 0),
    (Bz2FernetFile, 'library.pdf', 1024 * 1024, 0),
    (ZstdFernetFile, 'download.html', 1024 * 1024, 0),
    (ZstdFernetFile, 'genindex-all.html', 1024 * 1024, 0),
    (ZstdFernetFile, 'searchindex.js', 1024 * 1024, 0),
    (ZstdFernetFile, 'library.pdf', 1024 * 1024, 0),
])
def test_benchmark(random_path, fcls, dt, buff_size, file_size):
    key = Fernet.generate_key()
    if dt == 'rand':
        data = randbytes(file_size)
    elif '.pdf' in dt:
        fff = os.path.join('docs-pdf', dt)
        with open(fff,'rb') as ff:
            data = ff.read()
        file_size = os.path.getsize(fff)
    elif '.html' in dt or '.js' in dt:
        fff = os.path.join('python-3.13-docs-html', dt)
        with open(fff,'rb') as ff:
            data = ff.read()
        file_size = os.path.getsize(fff)
    else:
        data = dt * file_size
    dataf = os.path.join(random_path, 'test.frnt')
    time_start = time.time()
    with fcls(dataf, mode='wb', fernet_key=key, chunk_size=buff_size) as ff:
        ff.write(data)
    time_write = time.time()
    with fcls(dataf, "rb", fernet_key=key) as ff:
        datar = ff.read()
    time_read = time.time()
    assert data == datar
    comp_size = os.path.getsize(dataf)
    with open('BENCHMARK.md','at') as ff:
        ff.write("| %-20s | %-20s | %11.0f |  %10.0f | %10.0f | %10.2f%% | %6.2f | %6.2f |\n" % (("%s" % fcls).split('.')[-1][:-2], dt, buff_size / 1024, file_size / 1024, comp_size / 1024, comp_size / file_size * 100, time_write - time_start, time_read - time_write))

# ~ @pytest.mark.skip("Manual test")
@pytest.mark.skipif(not importlib.util.find_spec("pytest_ordering"), reason="requires the pytest_ordering package")
@pytest.mark.run(order=3)
@pytest.mark.parametrize("fcls, dt, buff_size, file_size", [
    (TarBz2FernetFile, 'html,js and pdf', 1024 * 16, 0),
    (TarBz2FernetFile, 'html,js and pdf', 1024 * 256, 0),
    (TarBz2FernetFile, 'html,js and pdf', 1024 * 1024, 0),
    (TarZstdFernetFile, 'html,js and pdf', 1024 * 16, 0),
    (TarZstdFernetFile, 'html,js and pdf', 1024 * 256, 0),
    (TarZstdFernetFile, 'html,js and pdf', 1024 * 1024, 0),
])
def test_benchmark_tar(random_path, fcls, dt, buff_size, file_size):
    key = Fernet.generate_key()
    dataf = os.path.join(random_path, 'test.frnt')
    time_start = time.time()
    with fcls(dataf, mode='w', fernet_key=key, chunk_size=buff_size) as ff:
        for tf in ['download.html', 'genindex-all.html', 'searchindex.js']:
            df = os.path.join('python-3.13-docs-html', tf)
            ff.add(df, tf)
            file_size += os.path.getsize(df)
        for tf in [ 'library.pdf']:
            df = os.path.join('docs-pdf', tf)
            ff.add(df, tf)
            file_size += os.path.getsize(df)
    time_write = time.time()
    with fcls(dataf, "r", fernet_key=key) as ff:
        ff.extractall('extract_tar')
    time_read = time.time()
    # ~ assert data == datar
    comp_size = os.path.getsize(dataf)
    for tf in ['download.html', 'genindex-all.html', 'searchindex.js']:
        with open(os.path.join('python-3.13-docs-html', tf),'rb') as ff:
            data = ff.read()
        with open(os.path.join('extract_tar', tf),'rb') as ff:
            datar = ff.read()
        assert data == datar
    for tf in [ 'library.pdf']:
        with open(os.path.join('docs-pdf', tf),'rb') as ff:
            data = ff.read()
        with open(os.path.join('extract_tar', tf),'rb') as ff:
            datar = ff.read()
        assert data == datar
    with open('BENCHMARK.md','at') as ff:
        ff.write("| %-20s | %-20s | %11.0f |  %10.0f | %10.0f | %10.2f%% | %6.2f | %6.2f |\n" % (("%s" % fcls).split('.')[-1][:-2], dt, buff_size / 1024, file_size / 1024, comp_size / 1024, comp_size / file_size * 100, time_write - time_start, time_read - time_write))

