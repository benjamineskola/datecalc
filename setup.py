# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="datecalc",
    version="0.0.1",
    description="calculate date differences",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/benjamineskola/datecalc",
    author="Benjamin Eskola",
    author_email="ben@eskola.uk",
    license="Creative Commons Attribution-NonCommercial 4.0 International",
    classifiers=["License :: Free for non-commercial use"],
    packages=find_packages(),
    python_requires=">=3.5, <4",
    install_requires=["python-dateutil"],
    entry_points={"console_scripts": ["datecalc=datecalc:main"]},
    project_urls={
        "Bug Reports": "https://gitlab.com/benjamineskola/datecalc/issues",
        "Source": "https://gitlab.com/benjamineskola/datecalc/",
    },
)
