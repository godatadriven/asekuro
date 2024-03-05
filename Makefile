test:
	poetry run pytest

check: test

deps:
	poetry install

clean:
	rm -rf build
	rm -rf asekuro.egg-info
	rm -rf .ipynb_checkpoints
	rm -rf .pytest_cache
	rm -rf dist
	rm -rf tests/.ipynb_checkpoints
	rm -rf notebooks/.ipynb_checkpoints
