from os.path import abspath, dirname, join

from setuptools import setup, find_packages

this_directory = abspath(dirname(__file__))
with open(join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='kaz',
    version='0.3.0.post0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['click'],
    entry_points='''
        [console_scripts]
        kaz=kaz.main:cli
    ''',
    # extra metadata
    description='A simple storage cli',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='storage cli',
    url='https://github.com/clabe45/kaz',
    author='Caleb Sacks',
    project_urls={
        'Bug Tracker': 'https://github.com/clabe45/kaz/issues'
    }
)
