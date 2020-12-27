from os.path import abspath, dirname, join

from setuptools import setup, find_packages

this_directory = abspath(dirname(__file__))
with open(join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='kaz',
    version='0.3.0.post2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['click', 'colorama'],
    entry_points='''
        [console_scripts]
        kaz=kaz.main:cli
    ''',
    # extra metadata
    description='A simple storage cli',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='storage store storing data cli tool minimalistic',
    url='https://github.com/clabe45/kaz',
    author='Caleb Sacks',
    license='GPLv3',
    project_urls={
        'Bug Tracker': 'https://github.com/clabe45/kaz/issues'
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: System',
        'Topic :: Utilities'
    ]
)
