# -*- encoding: utf-8 -*-
"""

.. include:: ../README.md
   :start-line: 1


"""
__author__ = 'bibi21000 aka Sébastien GALLET'
__email__ = 'bibi21000@gmail.com'

__all__ = ["FernetCryptor", "FernetFile", "open"]

import os

from cofferfile import EncryptFile, Cryptor, _open_t
from cofferfile import WRITE_BUFFER_SIZE, CHUNK_SIZE, READ, WRITE, APPEND, EXCLUSIVE # noqa F401
from cofferfile.decorator import reify

class FernetFile(EncryptFile):
    """
    `fernetfile.zstd`
    `fernetfile.tar`
    """

    def __init__(self, filename=None, mode=None, fileobj=None,
            chunk_size=CHUNK_SIZE, write_buffer_size=WRITE_BUFFER_SIZE,
            fernet_key=None,
        ):
        """Constructor for the FernetFile class.

        At least one of fileobj and filename must be given a
        non-trivial value.

        The new class instance is based on fileobj, which can be a regular
        file, an io.BytesIO object, or any other object which simulates a file.
        It defaults to None, in which case filename is opened to provide
        a file object.

        When fileobj is not None, the filename argument is only used to be
        included in the gzip file header, which may include the original
        filename of the uncompressed file.  It defaults to the filename of
        fileobj, if discernible; otherwise, it defaults to the empty string,
        and in this case the original filename is not included in the header.

        The mode argument can be any of 'r', 'rb', 'a', 'ab', 'w', 'wb', 'x', or
        'xb' depending on whether the file will be read or written.  The default
        is the mode of fileobj if discernible; otherwise, the default is 'rb'.
        A mode of 'r' is equivalent to one of 'rb', and similarly for 'w' and
        'wb', 'a' and 'ab', and 'x' and 'xb'.

        The fernet_key argument is the Fernet key used to crypt/decrypt data.

        Encryption is done by chunks to reduce memory footprint. The default
        chunk_size is 64KB.
        """
        super().__init__(filename=filename, mode=mode, fileobj=fileobj,
            chunk_size=chunk_size, write_buffer_size=write_buffer_size,
            cryptor='fernet', fernet_key=fernet_key)

    def __repr__(self):
        s = repr(self.myfileobj)
        return '<FernetFile ' + s[1:-1] + ' ' + hex(id(self)) + '>'

class FernetCryptor(Cryptor):

    @reify
    def _imp_cryptography_fernet(cls):
        """Lazy loader for cryptography.fernet"""
        import importlib
        return importlib.import_module('cryptography.fernet')

    @reify
    def _imp_cryptography_argon2(cls):
        """Lazy loader for cryptography.hazmat.primitives.kdf.argon2"""
        import importlib
        return importlib.import_module('cryptography.hazmat.primitives.kdf.argon2')

    def __init__(self, fernet_key=None, **kwargs):
        super().__init__(**kwargs)
        if fernet_key is None:
            raise ValueError("Invalid fernet_key: {!r}".format(fernet_key))
        self.fernet = self._imp_cryptography_fernet.Fernet(fernet_key)

    def derive(self, password, salt=None, key_len=64, iterations=1,
            lanes=4, memory_cost=64 * 1024):
        """Derive a key from password (experimental)
        See https://cryptography.io/en/latest/hazmat/primitives/key-derivation-functions/#argon2id
        """
        if salt is None:
            salt = self._imp_secrets.token_bytes(16)
        if isinstance(password, str):
            password = password.encode()
        kdf = self._imp_cryptography_argon2.Argon2id(
            salt=salt,
            length=key_len,
            iterations=iterations,
            lanes=lanes,
            memory_cost=memory_cost
        )
        return kdf.derive(password)

    def _decrypt(self, chunk):
        return self.fernet.decrypt(chunk)

    def _encrypt(self, chunk):
        return self.fernet.encrypt(chunk)



def open(filename, mode="rb", fernet_key=None,
         encoding=None, errors=None, newline=None,
         chunk_size=CHUNK_SIZE):
    """Open a Fernet file in binary or text mode.

    The filename argument can be an actual filename (a str or bytes object), or
    an existing file object to read from or write to.

    The mode argument can be "r", "rb", "w", "wb", "x", "xb", "a" or "ab" for
    binary mode, or "rt", "wt", "xt" or "at" for text mode. The default mode is
    "rb".

    For binary mode, this function is equivalent to the FernetFile constructor:
    FernetFile(filename, mode, fernet_key). In this case, the encoding, errors
    and newline arguments must not be provided.

    For text mode, a FernetFile object is created, and wrapped in an
    io.TextIOWrapper instance with the specified encoding, error handling
    behavior, and line ending(s).

    Encryption is done by chunks to reduce memory footprint. The default
    chunk_size is 64KB.
    """
    return _open_t(filename, mode=mode,
         encoding=encoding, errors=errors, newline=newline,
         chunk_size=chunk_size,
         cryptor='fernet', fernet_key=fernet_key)
