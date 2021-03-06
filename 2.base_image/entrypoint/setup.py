import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "htmesos-docker-entrypoint",
    version = "0.0.0",
    author = "Sara Vallero",
    author_email = "svallero@to.infn.it",
    description = ("Entrypoint for the HTMesos Docker container."),
    license = "",
    keywords = "",
    url = "",
    packages=['main'],
    long_description=read('README'),
    classifiers=[],
)
