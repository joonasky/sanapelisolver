from setuptools import setup, find_packages
from codecs import open
from os import path
import imp

here = path.abspath(path.dirname(__file__))

VERSIONFILE = path.join(here, 'src', 'sanapelisolver', '_version.py')


def get_version():
    return imp.load_source('_version', VERSIONFILE).get_version()


# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sanapelisolver',
    version=get_version(),
    description='Solve a Sanapeli game',
    long_description=long_description,
    url='https://github.com/joonasky/sanapelisolver',
    author='Joonas Kylliäinen',
    author_email='joonas@kylliainen.fi',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Author',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='solve game words',
    install_requires=[],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['sanapelisolver'],
    entry_points={
        'console_scripts': [
            'spsolve=sanapelisolver.sanapeli:main',
        ],
    },
)
