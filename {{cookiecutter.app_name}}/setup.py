# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

test_requirements = ['pytest>=3.1.1', 'pytest-cov>=2.5.1', 'codecov']
required = ['flask',
            'flask-bootstrap']

setup(
    name='{{cookiecutter.app_name}}',
    version='0.0.1',
    description=('{{cookiecutter.description}}'
                 'set of tools for compressing PDF files to e-reader friendly sizes.'),
    long_description=readme,
    author='Simon Larsén',
    author_email='slarse@kth.se',
    url='https://github.com/slarse/{{cookiecutter.app_name}}',
    #download_url='https://github.com/slarse/{cookiecutter.app_name}/archive/v0.1.0.tar.gz',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    tests_require=test_requirements,
    install_requires=required
)
