test:
	pytest

check: test

deps:
	pip install -e .

clean:
	rm -rf build
	rm -rf asekuro.egg-info
	rm -rf .ipynb_checkpoints
	rm -rf .pytest_cache
	rm -rf dist
	rm -rf tests/.ipynb_checkpoints
	rm -rf notebooks/.ipynb_checkpoints


develop: deps
	python setup.py develop
