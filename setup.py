import setuptools
import pathlib

setuptools.setup(
    name='imptools',
    version='1.3.0',
    author='Danijar Hafner',
    author_email='mail@danijar.com',
    description='Tools for improving Python imports.',
    url='http://github.com/danijar/imptools',
    long_description=pathlib.Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    packages=['imptools'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
