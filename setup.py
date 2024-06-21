import setuptools


setuptools.setup(
    name = 'TransportationHK',
    author = 'MaxPython110331',
    description = 'The python package(pypi) about Hong Kong\'s transportation.',
    long_description = open('README.md', 'r').read(),
    license = 'MIT',
    url = 'https://github.com/max-github110331/TransportationHK/',
    packages = [],
    version = '',
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires = [
        'requests'
    ],
    python_requires = '>=3.7' 
)