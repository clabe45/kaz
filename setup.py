from setuptools import setup, find_packages

setup(
    name='kaz',
    version='0.3.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['click'],
    entry_points='''
        [console_scripts]
        kaz=kaz.main:cli
    ''',
    # extra metadata
    description='A simple storage cli',
    keywords='storage cli',
    url='https://github.com/clabe45/kaz',
    author='Caleb Sacks',
    project_urls={
        'Bug Tracker': 'https://github.com/clabe45/kaz/issues'
    }
)
