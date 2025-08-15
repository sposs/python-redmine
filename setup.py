from setuptools import setup, find_packages

exec(open('redminelib/version.py').read())

setup(
    name='python-redmine',
    version=globals()['__version__'],
    packages=find_packages(exclude=('tests', 'tests.*')),
    url='https://github.com/maxtepkeev/python-redmine',
    project_urls={
        'Documentation': 'https://python-redmine.com',
    },
    license='Apache 2.0',
    author='Maxim Tepkeev',
    author_email='support@python-redmine.com',
    description='Library for communicating with a Redmine project management application',
    long_description_content_type='text/x-rst',
    long_description=open('README.rst').read() + '\n\n' + open('CHANGELOG.rst').read(),
    keywords='redmine redmineup redminecrm redminelib easyredmine',
    python_requires='>=3.7, <4',
    install_requires=['requests>=2.31.0'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Topic :: Internet :: WWW/HTTP',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
