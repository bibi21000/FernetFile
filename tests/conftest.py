# -*- encoding: utf-8 -*-
import pytest


@pytest.fixture
def random_path():
    """Fixture to execute asserts before and after a test is run"""
    import tempfile
    tmpdir = tempfile.TemporaryDirectory()
    yield tmpdir.name
    tmpdir.cleanup()
