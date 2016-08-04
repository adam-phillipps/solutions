from setuptools import setup
from codecs import open
from os import path

setup(name='solutions',
      version='0.1',
      description='Word count and meeting times challenges.',
      url='http://github.com/adam-phillipps/solutions',
      author='Adam Phillipps',
      author_email='adam.phillipps@gmail.com',
      license='MIT',
      packages=['solutions'],
      zip_safe=False)


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()
