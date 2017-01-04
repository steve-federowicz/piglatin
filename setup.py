import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='piglatin',

    version='0.0.1',

    description='Translate from english to piglatin',
    long_description=long_description,

    author='Steve Federowicz',
    author_email='sfederow@gmail.com',

    classifiers=[

        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='piglatin',

    packages=find_packages(),

    install_requires=['pytest'],

    entry_points={
        'console_scripts': [
            'piglatin = piglatin.translator:main',
        ],
    },
)
