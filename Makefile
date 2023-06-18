.PHONY: docs
init:
	python -m venv venv
	. venv/bin/activate && pip install --requirement requirements-dev.txt
	git submodule update --init --recursive

coverage:
	pytest --cov-report term --cov-report html --cov-report xml --cov=pysamplelib

build:
	pip install build
	python -m build

publish:
	pip install twine
	python -m twine upload --repository testpypi dist/*

docs:
	cd docs && make html
