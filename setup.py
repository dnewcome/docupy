import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "docupy",
    version = "0.0.1",
    author = "Dan Newcome",
    author_email = "dnewcome@circleup.com",
    description = ("A Python client library for Docusign."),
    license = "BSD",
    keywords = "docusign",
    url = "http://packages.python.org/docupy",
    packages=['docupy'],
    long_description = read('README.md'),
    install_requires = ['requests >= 1.2.3'],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Topic :: Clients",
        "License :: OSI Approved :: BSD License",
    ],
)
