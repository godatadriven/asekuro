test:
	pytest

flake:
	flake8 asekuro
	flake8 tests
	flake8 setup.py

check: flake test