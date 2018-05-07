application
================================

application is a `Websauna <https://websauna.org>`_ application package for application.

To run this package you need Python 3.4+, PostgresSQL and Redis.


Installation
============

This installation method assumes you the author of the application application and wish to develop it. Below are instructions to to install the package to a Python virtual environment using pip command in an editable mode.

Example:

    .. code-block:: shell

        cd application  # This is the folder with setup.py file
        python3 -m venv env  # Create virtual environment
        source env/bin/activate  # Activate virtual environment
        pip install -U pip  # Make sure pip itself is up-to-date
        pip install -e .  # Install this package


Running the website
===================

Local development machine
-------------------------

Create the database:

    .. code-block:: shell

        psql create application_dev  # Create database


.. note:: Edit the *application/application/conf/development.ini* file and change the connection string to the
          one used on your environment. i.e.: postgresql://username:passwd@localhost/application_dev


Sync models from this application to the newly created database:

    .. code-block:: shell

        ws-alembic -c application/application/conf/development.ini -x packages=all revision --auto -m "Initial migration"
        ws-alembic -c application/application/conf/development.ini -x packages=all upgrade head
        ws-sync-db ws://application/application/conf/development.ini


Add a user with administrative rights:

    .. code-block:: shell

        ws-create-user ws://application/application/conf/development.ini admin@example.com mypassword


Start the application:

    .. code-block:: shell

        pserve ws://application/application/conf/development.ini


Running the test suite
======================

First create test database:

    .. code-block:: shell

        # Create database used for unit testing
        psql create application_test


Install test and dev dependencies (run in the folder with ``setup.py``):

    .. code-block:: shell

        pip install -e ".[dev,test]"


Run test suite using py.test running:

    .. code-block:: shell

        py.test


More information
================

Please see https://websauna.org/
