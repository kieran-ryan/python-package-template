.PHONY: docs
init:
	python -m venv venv
	. venv/bin/activate && pip install --requirement requirements-dev.txt
	git submodule update --init --recursive
docs:
	cd docs && make html
