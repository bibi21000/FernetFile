[![CircleCI](https://dl.circleci.com/status-badge/img/gh/bibi21000/FernetFile/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/bibi21000/FernetFile/tree/main)
[![codecov](https://codecov.io/gh/bibi21000/FernetFile/graph/badge.svg?token=4124GIOJAK)](https://codecov.io/gh/bibi21000/FernetFile)

# FernetFile
A python xxxFile like (ie GzipFile, BZ2File, ...) for encrypting files with Fernet.

 - encrypting / decrypting data using chunks to reduce memory footprint
 - chainable with other python xxxFile interfaces


## create your encryption key


    from cryptography.fernet import Fernet

    key = Fernet.generate_key()

and store it in a safe place (disk, database, ...).

This key is essential to encrypt and decrypt data.
Losing this key means losing the data.

## "open" your crytpted files like normal files

### Text files

    ```python

    import fernetfile

    with fernetfile.open('test.txc', mode='wt', fernet_key=key, encoding="utf-8") as ff:
        ff.write(data)

    with fernetfile.open('test.txc', "rt", fernet_key=key, encoding="utf-8") as ff:
        data = ff.read()

    with fernetfile.open('test.txc', mode='wt', fernet_key=key, encoding="utf-8") as ff:
        ff.writelines(data)

    with fernetfile.open('test.txc', "rt", fernet_key=key, encoding="utf-8") as ff:
        data = ff.readlines()

    ```

### Binary files

>    import fernetfile
>
>    with fernetfile.open('test.dac', mode='wb', fernet_key=key) as ff:
>        ff.write(data)
>
>    with fernetfile.open('test.dac', "rb", fernet_key=key) as ff:
>        data = ff.read()

## Use the xxxFile like interface

>    import fernetfile
>
>    with fernetfile.FernetFile('test.dac', mode='wb', fernet_key=key) as ff:
>        ff.write(data)
>
>    with fernetfile.FernetFile('test.dac', mode='rb', fernet_key=key) as ff:
>        data = ff.read()

## Chain to compress and encrypt

>    import fernetfile
>    import bz2
>
>    class Bz2FernetFile(bz2.BZ2File):
>
>        def __init__(self, name, mode='r', fernet_key=None, chunk_size=fernetfile.CHUNK_SIZE, \**kwargs):
>            compresslevel = kwargs.pop('compresslevel', 9)
>            self.fernet_file = fernetfile.FernetFile(name, mode,
>                fernet_key=fernet_key, chunk_size=chunk_size, \**kwargs)
>            try:
>                super().__init__(self.fernet_file, mode=mode,
>                    compresslevel=compresslevel, \**kwargs)
>            except Exception:
>                self.fernet_file.close()
>                raise
>
>        def close(self):
>            try:
>                super().close()
>            finally:
>                if self.fernet_file is not None:
>                    self.fernet_file.close()
>
>
>    with Bz2FernetFile('test.bzc', mode='wb', fernet_key=key) as ff:
>        ff.write(data)
>
>    with Bz2FernetFile('test.bzc', mode='rb', fernet_key=key) as ff:
>        data = ff.read()

## Chain to tar and compress and encrypt

>    import fernetfile
>    import bz2
>    import tarfile
>
>    class TarBz2FernetFile(tarfile.TarFile):
>
>        def __init__(self, name, mode='r', fernet_key=None, chunk_size=fernetfile.CHUNK_SIZE, \**kwargs):
>            compresslevel = kwargs.pop('compresslevel', 9)
>            self.fernet_file = fernetfile.FernetFile(name, mode,
>                fernet_key=fernet_key, chunk_size=chunk_size, \**kwargs)
>            try:
>                self.bz2_file = bz2.BZ2File(self.fernet_file, mode=mode,
>                    compresslevel=compresslevel, \**kwargs)
>                try:
>                    super().__init__(fileobj=self.bz2_file, mode=mode, \**kwargs)
>
>                except Exception:
>                    self.bz2_file.close()
>                    raise
>
>            except Exception:
>                self.fernet_file.close()
>                raise
>
>        def close(self):
>            try:
>                super().close()
>            finally:
>                try:
>                    if self.fernet_file is not None:
>                        self.bz2_file.close()
>                finally:
>                    if self.fernet_file is not None:
>                        self.fernet_file.close()
>
>
>    with TarBz2FernetFile('test.bzc', mode='wb', fernet_key=key) as ff:
>        ff.add(dataf1, 'file1.out')
>        ff.add(dataf2, 'file2.out')
>
>    with TarBz2FernetFile('test.bzc', mode='rb', fernet_key=key) as ff:
>        fdata1 = ff.extractfile('file1.out')
>        fdata2 = ff.extractfile('file2.out')

