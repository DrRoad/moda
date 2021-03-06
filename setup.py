from setuptools import setup

# read the contents of the README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
    #print(long_description)

setup(
    name='moda',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.2.2',
    packages=['moda.dataprep',
              'moda.evaluators',
              'moda.models'
              ],
    url='https://www.github.com/omri374/moda',
    license='MIT',
    author='Omri Mendels',
    author_email='omri.mendels@microsoft.com',
    description='Tools for analyzing trending topics',
    install_requires=['numpy', 'pandas', 'stldecompose', 'statsmodels', 'comet_ml', 'requests', 'matplotlib', 'pytest',
                      'pytest-cov']

)
