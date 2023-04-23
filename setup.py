"""Library build script."""

from __future__ import annotations

from pathlib import Path

import setuptools

# Extract README content
repository_base_dir = Path(__file__).parent
README = (repository_base_dir / "README.md").read_text()

# Extract library metadata
source_base_dir = repository_base_dir / "pysamplelib"
metadata: dict[str, str] = {}
with (source_base_dir / "__version__.py").open() as version_file:
    exec(version_file.read(), metadata)  # nosec: B102

setuptools.setup(
    name=metadata["__title__"],
    version=metadata["__version__"],
    author=metadata["__author__"],
    description=metadata["__description"],
    long_description=README,
    long_description_content_type="text/markdown",
    url=metadata["__url__"],
    license=metadata["__license__"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
    ],
    packages=[metadata["__title__"]],
    include_package_data=True,
)
