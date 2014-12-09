from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='typefinder',
      version='0.1',
      description='Locate, validate and clean various network types',
      url='https://github.com/heyglen/TypeFinder',
      author='Glen Harmon',
      long_description=readme(),
      license='MIT',
      packages=['typefinder'],
      install_requires=[
          'ipaddress',
      ],
      zip_safe=False)
