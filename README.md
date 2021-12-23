# Python Library Template

![Release version](https://img.shields.io/badge/version-0.0.0-green)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python version](https://img.shields.io/badge/python-3.10-blue)
![Supported platforms](https://img.shields.io/badge/platforms-macOS%20%7C%20Windows%20%7C%20Linux-green)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

A template repository for creating Python libraries.

## Features

- Common repository files:
  - `.gitignore` with common files to be excluded by git for Python
  - `.pre-commit-config.yaml` with common pre-commit validation for Python
  - `LICENSE` outlining usage rights
  - `Makefile` standardising commands
  - `OWNERS.md` outlining owners and roles
  - `README.md` overview documentation
- Static analysis tool configuration:
  - [Sphinx](https://www.sphinx-doc.org/en/master/) - documentation
  - [flake8](https://flake8.pycqa.org/en/latest/) - [PEP8](https://www.python.org/dev/peps/pep-0008/) compliance
  - [flake8-comprehensions](https://pypi.org/project/flake8-comprehensions/) - comprehension checking
  - [flake8-docstrings](https://github.com/PyCQA/flake8-docstrings) - [PEP257](https://www.python.org/dev/peps/pep-0257/) compliance
  - [flake8-return](https://pypi.org/project/flake8-return/) - return value checking
  - [flake8-sfs](https://pypi.org/project/flake8-sfs/) - single string format checking
  - [isort](https://pycqa.github.io/isort/) - [PEP8](https://www.python.org/dev/peps/pep-0008/) import compliance
  - [mypy](https://mypy.readthedocs.io) - type checking
  - [bandit](https://bandit.readthedocs.io/en/latest/) - common security issue detection
  - [black](https://black.readthedocs.io/en/stable/) - code style formatting
  - [pycln](https://hadialqattan.github.io/pycln/#/) - unused import detection
  - [pep8-naming](https://pypi.org/project/pep8-naming/) - [PEP8](https://www.python.org/dev/peps/pep-0008/) naming compliance
  - [pyupgrade](https://github.com/asottile/pyupgrade) - latest syntax upgrades
  - [radon](https://pypi.org/project/radon/) - code quality metrics
  - [coverage](https://coverage.readthedocs.io/en/6.2/) - test coverage metrics
- Examples:
  - Repository tree structure
  - Python module
  - Unit tests

## License

`python-library-template` is licensed under the [MIT License](https://opensource.org/licenses/MIT)
