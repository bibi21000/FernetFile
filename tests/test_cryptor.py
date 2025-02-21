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

def test_cryptor_bad(random_path, random_name):
    key = Fernet.generate_key()
    cryptor = Cryptor(fernet_key=key)

    with pytest.raises(TypeError):
        derive = cryptor.derive(None)
