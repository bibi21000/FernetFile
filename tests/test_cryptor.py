# -*- encoding: utf-8 -*-
"""Test module

"""
import os
import io

from cryptography.fernet import Fernet, InvalidToken

from fernetfile import FernetCryptor as Cryptor

import pytest


def test_cryptor(random_path, random_name):
    key = Fernet.generate_key()
    cryptor = Cryptor(fernet_key=key)
    derive = cryptor.derive('test')

def test_cryptor_class(random_path, random_name):
    derive = Cryptor.derive('test')
    with pytest.raises(TypeError):
        derive = Cryptor.derive(None)

def test_cryptor_bad(random_path, random_name):
    key = Fernet.generate_key()
    cryptor = Cryptor(fernet_key=key)

    with pytest.raises(TypeError):
        derive = cryptor.derive(None)

def test_cryptor_derive(random_path, random_name):
    import secrets
    salt, derive1 = Cryptor.derive('test')
    _, derive2 = Cryptor.derive('test', salt=salt)
    crypt1 = Cryptor(fernet_key=derive1)
    crypt2 = Cryptor(fernet_key=derive2)
    text = secrets.token_bytes(1785)
    crypted = crypt1._encrypt(text)
    uncrypted = crypt1._decrypt(crypted)
    assert uncrypted == text
    uncrypted = crypt2._decrypt(crypted)
    assert uncrypted == text
