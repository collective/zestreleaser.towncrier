Developing this package
-----------------------

Create a virtualenv in the package::

    $ virtualenv --clear .

Install requirements with pip::

    $ ./bin/pip install -r requirements.txt

Install the package under development::

    $ ./bin/python setup.py develop

Use this plugin while release a package::

    $ ./bin/fullrelease
