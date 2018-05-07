"""Another Websauna application.."""
from setuptools import find_packages
from setuptools import setup

import os
import sys

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.rst')) as f:
    CHANGES = f.read()

# trying to run python setup.py install or python setup.py develop
if len(sys.argv) >= 2:
    if sys.argv[0] == 'setup.py' and sys.argv[1] in ('install', 'develop'):
        # Otherwise so much stuff would be broken later...
        raise RuntimeError(
            'It is not possible to install this package with setup.py. '
            'Use pip to install this package as instructed in Websauna tutorial.'
        )


requires = [
    'prettyconf',
    'websauna',
]

dev_requirements = [
    'websauna[dev]',
    'zest.releaser[recommended]',
]

test_requirements = [
    'flake8',
    'pytest',
    'pytest-runner',
    'pytest-splinter',
    'webtest',
]

setup(
    name='application',
    version='1.0.0',
    description='',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Pyramid',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='Amazing Team',
    author_email='team@mycompany.com',
    url='',
    keywords='python package websauna pyramid',
    packages=find_packages(),
    namespace_packages=['application', ],
    include_package_data=True,
    zip_safe=False,
    test_suite='application',
    extras_require={
        # Dependencies for running test suite
        'test': test_requirements,
        # Dependencies to make releases
        'dev': dev_requirements,
    },
    install_requires=requires,
    entry_points="""\
        [paste.app_factory]
        main = application.application:main
    """,
)
