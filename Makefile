#!/usr/bin/make -f

venv:
	python3 -m venv venv
	./venv/bin/pip install .
	./venv/bin/pip install .[test]
	./venv/bin/pip install .[zstd]

build:
	rm -rf dist
	./venv/bin/python3 -m build

testpypi:
	./venv/bin/python3 -m twine upload --repository testpypi --verbose dist/*

doc:
	./venv/bin/pdoc --output-directory docs fernetfile/zstd.py fernetfile/__init__.py

pypi:
	./venv/bin/python3 -m twine upload --repository pypi --verbose dist/*
