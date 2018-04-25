#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import country_dialcode
import os
import re


def read(*parts):
    return open(os.path.join(os.path.dirname(__file__), *parts, encoding="utf-8")).read()


def parse_requirements(file_name):
    requirements = []
    for line in open(file_name, 'r').read().split('\n'):
        if re.match(r'(\s*#)|(\s*$)', line):
            continue
        if re.match(r'\s*-e\s+', line):
            requirements.append(re.sub(r'\s*-e\s+.*#egg=(.*)$', r'\1', line))
        elif re.match(r'(\s*git)|(\s*hg)', line):
            pass
        else:
            requirements.append(line)
    return requirements


def parse_dependency_links(file_name):
    dependency_links = []
    for line in open(file_name, 'r').read().split('\n'):
        if re.match(r'\s*-[ef]\s+', line):
            dependency_links.append(re.sub(r'\s*-[ef]\s+', '', line))

    return dependency_links


setup(
    name='django-country-dialcode',
    version=country_dialcode.__version__,
    description='Django Application providing Dialcode and Countries code',
    long_description=read('README.rst'),
    author='Belaid Arezqui',
    author_email='areski@gmail.com',
    url='http://github.com/Star2Billing/django-country-dialcode',
    zip_safe=False,
    packages=find_packages(exclude=["tests", "docs"]),
    package_data={
        "": [
            "fixtures/*",
        ]
    },
    # install_requires=parse_requirements('requirements.txt'),
    # dependency_links=parse_dependency_links('requirements.txt'),
    include_package_data=True,
    license='MIT License',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
