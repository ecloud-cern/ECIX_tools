from setuptools import setup, find_packages

setup(
    name='ECIX_tools',
    version="2.1",
    description='Tools for e-cloud simulations in xsuite',
    long_description='Tools for e-cloud simulations in xsuite',
    author='K. Paraschou',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'h5py'
    ],
    url='https://github.com/ecloud-cern/ECIX_tools',
)
