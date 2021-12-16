.PHONY: docs
init:
	pip install --requirement requirements.txt
docs:
	cd docs && make html
