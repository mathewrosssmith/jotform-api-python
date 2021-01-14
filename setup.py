from setuptools import setup, find_packages

description = 'JotForm API - Python 3 Client'
try:
    with open("README.md", "r") as f:
        long_description = f.read()
except:
    long_description = description

setup(
    name="jotform",
    url='http://github.com/mathewrosssmith/jotform-api-python3',
    version='2.0',
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Mathew Smith',
    author_email='msmith@btech.edu',
    packages=find_packages(),
    py_modules=['jotform'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
