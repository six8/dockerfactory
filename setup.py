import re
from setuptools import setup, find_packages
from codecs import open

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

with open('dockerfactory/__init__.py', 'r') as fd:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
        fd.read(), re.MULTILINE).group(1)

setup(
    name='dockerfactory',
    long_description=readme,
    author='Michael Thornton',
    description='Control the context of your docker builds.',
    license='MIT',
    author_email='six8@devdetails.com',
    url='https://github.com/six8/dockerfactory',
    packages=find_packages(),
    package_dir={'': '.'},
    version=version,
    install_requires=[
        'click>=6.2,<7',
        'pyyaml>=3.11,<4',
        'schematics>=1.1.1,<2',
    ],
    entry_points={
        'console_scripts': [
            'dockerfactory = dockerfactory.__main__:cli',
        ]
    }
)
