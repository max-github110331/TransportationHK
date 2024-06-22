import setuptools


setuptools.setup(
    name = 'TransportationHK',
    author = 'MaxPython110331',
    description = 'The python package(pypi) about Hong Kong\'s transportation.',
    long_description = open('README.md', 'r').read(),
    long_description_content_type="text/markdown",
    license = 'MIT',
    url = 'https://github.com/max-github110331/TransportationHK/',
    packages = ['KMB'],
    version = '0.0.0b1',
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