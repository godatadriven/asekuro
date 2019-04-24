test:
	pytest

check: test

deps:
	pip install -e .

develop: deps
	python setup.py develop