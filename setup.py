# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='AudioLog',
    version='0.0.1',
    description='AudioLog skill for Alexa',
    long_description=readme,
    author='James Wu',
    author_email='james@meiji.software',
    url='https://github.com/SavvyGuard/AudioLog',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

