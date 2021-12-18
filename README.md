# Python Library Template

![License](https://img.shields.io/badge/license-MIT-blue)
![Python version](https://img.shields.io/badge/python-3.10-blue)
![Supported platforms](https://img.shields.io/badge/platforms-macOS%20%7C%20Windows%20%7C%20Linux-green)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)
![Release version](https://img.shields.io/badge/version-0.0.0-green)

A template repository for creating Python libraries.

## Features

- Common repository files:
  - `.gitignore` with common files to be excluded by git for Python
  - `.pre-commit-config.yaml` with common pre-commit validation for Python
  - `LICENSE` outlining usage rights
  - `Makefile` standardising commands
  - `OWNERS.md` outlining owners and roles
  - `README.md` outlining purpose and description
- Static analysis tool configuration:
  - [Sphinx](https://www.sphinx-doc.org/en/master/) - documentation
  - [flake8](https://flake8.pycqa.org/en/latest/) - [PEP8](https://www.python.org/dev/peps/pep-0008/) compliance
  - [flake8-comprehensions](https://pypi.org/project/flake8-comprehensions/) - comprehension checking
  - [flake8-docstrings](https://github.com/PyCQA/flake8-docstrings) - [PEP257](https://www.python.org/dev/peps/pep-0257/) compliance
  - [mypy](https://mypy.readthedocs.io) - static type checking
  - [bandit](https://bandit.readthedocs.io/en/latest/) - common security issue detection
  - [black](https://black.readthedocs.io/en/stable/) - code style formatting
  - [radon](https://pypi.org/project/radon/) - code quality metrics
  - [coverage](https://coverage.readthedocs.io/en/6.2/) - test coverage metrics
- Examples:
  - Repository tree structure
  - Python module
  - Unit tests

## License

`python-library-template` is licensed under the [MIT License](https://opensource.org/licenses/MIT)
