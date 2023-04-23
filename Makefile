.PHONY: docs
init:
	python -m venv venv
	. venv/bin/activate && pip install --requirement requirements-dev.txt
	git submodule update --init --recursive

coverage:
	pytest --cov-report term --cov-report html --cov-report xml --cov=pysamplelib

publish:
	pip install twine
	pip install build
	python -m build
	python -m twine upload --repository testpypi dist/*
	rm -rf dist pysamplelib.egg-info

docs:
	cd docs && make html
