.PHONY: docs
init:
	python -m venv venv
	. venv/bin/activate && pip install --requirement requirements-dev.txt
docs:
	cd docs && make html
