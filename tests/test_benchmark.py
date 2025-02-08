# -*- encoding: utf-8 -*-
"""Test module

"""
import os
import importlib
import time
from random import randbytes
import urllib.request
import zipfile

from cryptography.fernet import Fernet

import fernetfile

import pytest
from fernetfile.zstd import FernetFile as _ZstdFernetFile, CParameter, open as zstd_open
from fernetfile.store import TarZstdFernetFile, FernetStore
from .test_chain import Bz2FernetFile, LzmaFernetFile, TarBz2FernetFile, TarLzmaFernetFile

class ZstdFernetFile(_ZstdFernetFile):
    pass

# ~ @pytest.mark.skip("Manual test")
@pytest.mark.skipif(not importlib.util.find_spec("pytest_ordering"), reason="requires the pytest_ordering package")
@pytest.mark.run(order=21)
def test_benchmark_header(random_path):
    with open('BENCHMARK.md','at') as ff:
        ff.write("\n")
        ff.write("\n")
        ff.write("# General benchmarks\n")
        ff.write("\n")
        ff.write("| Class                | Data                 |  Chunk size |  Orig size  | Crypt size |  Comp ratio | WTime  | Rtime  |\n")
        ff.write("|:---------------------|:---------------------|------------:|------------:|-----------:|------------:|-------:|-------:|\n")
    if os.path.isfile('docpython.pdf.zip') is False:
        urllib.request.urlretrieve("https://docs.python.org/3/archives/python-3.13-docs-pdf-a4.zip", "docpython.pdf.zip")
        with zipfile.ZipFile('docpython.pdf.zip', 'r') as zip_ref:
            zip_ref.extractall('.')
    if os.path.isfile('docpython.html.zip') is False:
        urllib.request.urlretrieve("https://docs.python.org/3/archives/python-3.13-docs-html.zip", "docpython.html.zip")
        with zipfile.ZipFile('docpython.html.zip', 'r') as zip_ref:
            zip_ref.extractall('.')

# ~ @pytest.mark.skip("Manual test")
@pytest.mark.skipif(not importlib.util.find_spec("pytest_ordering"), reason="requires the pytest_ordering package")
@pytest.mark.run(order=22)
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
    (LzmaFernetFile, 'download.html', 1024 * 16, 0),
    (LzmaFernetFile, 'genindex-all.html', 1024 * 16, 0),
    (LzmaFernetFile, 'searchindex.js', 1024 * 16, 0),
    (LzmaFernetFile, 'library.pdf', 1024 * 16, 0),
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
    (LzmaFernetFile, 'download.html', 1024 * 256, 0),
    (LzmaFernetFile, 'genindex-all.html', 1024 * 256, 0),
    (LzmaFernetFile, 'searchindex.js', 1024 * 256, 0),
    (LzmaFernetFile, 'library.pdf', 1024 * 256, 0),
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
    (LzmaFernetFile, 'download.html', 1024 * 1024, 0),
    (LzmaFernetFile, 'genindex-all.html', 1024 * 1024, 0),
    (LzmaFernetFile, 'searchindex.js', 1024 * 1024, 0),
    (LzmaFernetFile, 'library.pdf', 1024 * 1024, 0),
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
@pytest.mark.run(order=23)
@pytest.mark.parametrize("fcls, dt, buff_size, file_size", [
    (TarBz2FernetFile, 'html,js and pdf', 1024 * 16, 0),
    (TarBz2FernetFile, 'html,js and pdf', 1024 * 256, 0),
    (TarBz2FernetFile, 'html,js and pdf', 1024 * 1024, 0),
    (TarZstdFernetFile, 'html,js and pdf', 1024 * 16, 0),
    (TarZstdFernetFile, 'html,js and pdf', 1024 * 256, 0),
    (TarZstdFernetFile, 'html,js and pdf', 1024 * 1024, 0),
    (TarLzmaFernetFile, 'html,js and pdf', 1024 * 16, 0),
    (TarLzmaFernetFile, 'html,js and pdf', 1024 * 256, 0),
    (TarLzmaFernetFile, 'html,js and pdf', 1024 * 1024, 0),
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


@pytest.mark.skipif(not importlib.util.find_spec("pytest_ordering"), reason="requires the pytest_ordering package")
@pytest.mark.run(order=10)
def test_benchmark_zstd_header(random_path):
    with open('BENCHMARK.md','at') as ff:
        ff.write("\n")
        ff.write("\n")
        ff.write("# Benchmarks ZstdFernetFile\n")
        ff.write("\n")
        ff.write("Tests with different compression level and workers\n")
        ff.write("\n")
        ff.write("| Class                | Data                 | Lvl | Wrks |  Orig size  | Crypt size |  Comp ratio | WTime  | Rtime  |\n")
        ff.write("|:---------------------|:---------------------|----:|-----:|------------:|-----------:|------------:|-------:|-------:|\n")
    if os.path.isfile('docpython.pdf.zip') is False:
        urllib.request.urlretrieve("https://docs.python.org/3/archives/python-3.13-docs-pdf-a4.zip", "docpython.pdf.zip")
        with zipfile.ZipFile('docpython.pdf.zip', 'r') as zip_ref:
            zip_ref.extractall('.')
    if os.path.isfile('docpython.html.zip') is False:
        urllib.request.urlretrieve("https://docs.python.org/3/archives/python-3.13-docs-html.zip", "docpython.html.zip")
        with zipfile.ZipFile('docpython.html.zip', 'r') as zip_ref:
            zip_ref.extractall('.')



# ~ @pytest.mark.skip("Manual test")
@pytest.mark.skipif(not importlib.util.find_spec("pytest_ordering"), reason="requires the pytest_ordering package")
@pytest.mark.run(order=11)
@pytest.mark.parametrize("fcls, dt, lvl, wrks", [
    (ZstdFernetFile, 'genindex-all.html', 9, 2),
    (ZstdFernetFile, 'genindex-all.html', 9, 8),
    (ZstdFernetFile, 'genindex-all.html', 9, 12),
    (ZstdFernetFile, 'genindex-all.html', 19, 2),
    (ZstdFernetFile, 'genindex-all.html', 19, 8),
    (ZstdFernetFile, 'genindex-all.html', 19, 12),
    (ZstdFernetFile, 'searchindex.js', 9, 2),
    (ZstdFernetFile, 'searchindex.js', 9, 8),
    (ZstdFernetFile, 'searchindex.js', 9, 12),
    (ZstdFernetFile, 'searchindex.js', 19, 2),
    (ZstdFernetFile, 'searchindex.js', 19, 8),
    (ZstdFernetFile, 'searchindex.js', 19, 12),
    (ZstdFernetFile, 'library.pdf', 9, 2),
    (ZstdFernetFile, 'library.pdf', 9, 8),
    (ZstdFernetFile, 'library.pdf', 9, 12),
    (ZstdFernetFile, 'library.pdf', 19, 2),
    (ZstdFernetFile, 'library.pdf', 19, 8),
    (ZstdFernetFile, 'library.pdf', 19, 12),
])
def test_benchmark_zstd_tar(random_path, fcls, dt, lvl, wrks):
    key = Fernet.generate_key()
    dataf = os.path.join(random_path, 'test.frnt')
    time_start = time.time()
    level_or_option = {
        CParameter.compressionLevel : lvl,
        CParameter.nbWorkers : wrks
    }
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
    with fcls(dataf, mode='wb', fernet_key=key, level_or_option=level_or_option) as ff:
        ff.write(data)
    time_write = time.time()
    level_or_option = {
        # ~ DParameter.windowLogMax : 0,
    }
    with fcls(dataf, "rb", fernet_key=key, level_or_option=level_or_option) as ff:
    # ~ with fcls(dataf, "rb", fernet_key=key) as ff:
        datar = ff.read()
    time_read = time.time()
    assert data == datar
    comp_size = os.path.getsize(dataf)
    with open('BENCHMARK.md','at') as ff:
        ff.write("| %-20s | %-20s | %3.0f | %4.0f |  %10.0f | %10.0f | %10.2f%% | %6.2f | %6.2f |\n" % (("%s" % fcls).split('.')[-1][:-2], dt, lvl, wrks, file_size / 1024, comp_size / 1024, comp_size / file_size * 100, time_write - time_start, time_read - time_write))


@pytest.mark.skipif(not importlib.util.find_spec("pytest_ordering"), reason="requires the pytest_ordering package")
@pytest.mark.run(order=0)
def test_benchmark_fstore_header(random_path):
    with open('BENCHMARK.md','wt') as ff:
        ff.write("# Benchmarks FernetStore\n")
        ff.write("\n")
        ff.write("Tests done with autoflush, with or without open_secure.\n")
        ff.write("\n")
        ff.write("WT -1, ... are the last store.add time in store\n")
        ff.write("\n")
        ff.write("WTime is the total write time. RTime the time spent to read\n")
        ff.write("\n")
        ff.write("| Data              | NbDocs | Op sec | Orig size | Crypt size | C Ratio | WTime | Rtime | WT -1 | WT -2 | WT -3 | WT -4 |\n")
        ff.write("|:------------------|-------:|-------:|----------:|-----------:|--------:|------:|------:|------:|------:|------:|------:|\n")
    if os.path.isfile('docpython.pdf.zip') is False:
        urllib.request.urlretrieve("https://docs.python.org/3/archives/python-3.13-docs-pdf-a4.zip", "docpython.pdf.zip")
        with zipfile.ZipFile('docpython.pdf.zip', 'r') as zip_ref:
            zip_ref.extractall('.')
    if os.path.isfile('docpython.html.zip') is False:
        urllib.request.urlretrieve("https://docs.python.org/3/archives/python-3.13-docs-html.zip", "docpython.html.zip")
        with zipfile.ZipFile('docpython.html.zip', 'r') as zip_ref:
            zip_ref.extractall('.')


# ~ @pytest.mark.skip("Manual test")
@pytest.mark.skipif(not importlib.util.find_spec("pytest_ordering"), reason="requires the pytest_ordering package")
@pytest.mark.run(order=1)
@pytest.mark.parametrize("dt, key, secure_open, secure_params, nb_doc", [
    ('genindex-all.html', Fernet.generate_key(), None, None, 5),
    ('genindex-all.html', Fernet.generate_key(), zstd_open, {'fernet_key':Fernet.generate_key()}, 5),
    ('genindex-all.html', Fernet.generate_key(), fernetfile.open, {'fernet_key':Fernet.generate_key()}, 5),
    ('genindex-all.html', Fernet.generate_key(), None, None, 20),
    ('genindex-all.html', Fernet.generate_key(), zstd_open, {'fernet_key':Fernet.generate_key()}, 20),
    ('genindex-all.html', Fernet.generate_key(), fernetfile.open, {'fernet_key':Fernet.generate_key()}, 20),
    ('searchindex.js', Fernet.generate_key(), None, None, 5),
    ('searchindex.js', Fernet.generate_key(), zstd_open, {'fernet_key':Fernet.generate_key()}, 5),
    ('searchindex.js', Fernet.generate_key(), fernetfile.open, {'fernet_key':Fernet.generate_key()}, 5),
    ('searchindex.js', Fernet.generate_key(), None, None, 20),
    ('searchindex.js', Fernet.generate_key(), zstd_open, {'fernet_key':Fernet.generate_key()}, 20),
    ('searchindex.js', Fernet.generate_key(), fernetfile.open, {'fernet_key':Fernet.generate_key()}, 20),
    ('library.pdf', Fernet.generate_key(), None, None, 5),
    ('library.pdf', Fernet.generate_key(), zstd_open, {'fernet_key':Fernet.generate_key()}, 5),
    ('library.pdf', Fernet.generate_key(), fernetfile.open, {'fernet_key':Fernet.generate_key()}, 5),
    ('library.pdf', Fernet.generate_key(), None, None, 20),
    ('library.pdf', Fernet.generate_key(), zstd_open, {'fernet_key':Fernet.generate_key()}, 20),
    ('library.pdf', Fernet.generate_key(), fernetfile.open, {'fernet_key':Fernet.generate_key()}, 20),
])
def test_benchmark_fstore(random_path, dt, key, secure_open, secure_params, nb_doc):
    dataf = os.path.join(random_path, 'test.frnt')
    time_start = time.time()
    times = []
    file_size = 0
    with FernetStore(dataf, mode='w', fernet_key=key,
            secure_open=secure_open, secure_params=secure_params) as ff:
        for i in range(nb_doc):
            if dt in ['download.html', 'genindex-all.html', 'searchindex.js']:
                df = os.path.join('python-3.13-docs-html', dt)
                ff.add(df, dt + '%s'%i)
                file_size += os.path.getsize(df)
            elif dt in [ 'library.pdf']:
                df = os.path.join('docs-pdf', dt)
                ff.add(df, dt + '%s'%i)
                file_size += os.path.getsize(df)
            times.append(time.time())
    time_write = time.time()
    with FernetStore(dataf, "rb", fernet_key=key,
            secure_open=secure_open, secure_params=secure_params) as ff:
        ff.extractall('extract_tar')
    time_read = time.time()
    # ~ assert data == datar
    comp_size = os.path.getsize(dataf)
    for i in range(nb_doc):
        if dt in ['download.html', 'genindex-all.html', 'searchindex.js']:
            with open(os.path.join('python-3.13-docs-html', dt),'rb') as ff:
                data = ff.read()
            with open(os.path.join('extract_tar', dt + '%s'%i),'rb') as ff:
                datar = ff.read()
            assert data == datar
        elif dt in [ 'library.pdf']:
            with open(os.path.join('docs-pdf', dt),'rb') as ff:
                data = ff.read()
            with open(os.path.join('extract_tar', dt + '%s'%i),'rb') as ff:
                datar = ff.read()
            assert data == datar
    if secure_open == zstd_open:
        sopen = 'zstd'
    elif secure_open == fernetfile.open:
        sopen = 'frnt'
    else:
        sopen = 'None'
    with open('BENCHMARK.md','at') as ff:
        ff.write("|%-18s | %6.0f | %-6s | %9.0f |  %9.0f | %7.2f | %5.2f | %5.2f | %5.2f | %5.2f | %5.2f | %5.2f |\n" %
        (dt, nb_doc, sopen, file_size / 1024, comp_size / 1024, comp_size / file_size * 100,
        time_write - time_start, time_read - time_write, times[-1] - times[-2], times[-2] - times[-3], times[-3] - times[-4], times[-4] - times[-5]))
