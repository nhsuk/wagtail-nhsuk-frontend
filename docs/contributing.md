# Contributing

## The test app

There is a test app inside the `testapp` directory. It is a default wagtail
installation with the wagtail-nhs-style app installed.

CSS must be built by running `python setup.py build` in the project root directory.

Install the test app dependencies by running `pip install -r requirements.txt` in the `testapp` directory. This will install the local `wagtailnhsukfrontend` module in [edit mode](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs) so that you can make changes to the module and see them immediately in the testapp.

Run `python manage.py runserver 8080` inside the `testapp` directory to start
the app on http://localhost:8080

To install the test fixture, make sure you have an empty but fully migrated database.

Run `python manage.py loaddata testdata.json`.

You should now have sample content pages in your wagtail installation.

The default login is username="admin" and password="password123"

## Scope

This project is a wagtail implementation of [nhsuk-frontend](https://github.com/nhsuk/nhsuk-frontend).

Only components developed and accepted into the NHSUK Frontend will appear in this library.

## New components

If you are creating new functionality for this package, you must make sure the
components can be tested in the testapp by (where appropriate):
 - Adding python code to the `testapp/home/models.py`.
 - Adding page content to the data fixture.
 - Using templatetags in the testapp templates.
 - Using template includes in the testapp templates.

To add to the fixture, either:
 - edit `testdata.json` by hand (useful for small changes)
 - run the dumpdata script `./dumpdata.sh > testdata.json`

Always review your changes to the testdata before committing to make sure there
are no accidental changes to the fixture.

## Python

Python code should be of [PEP8](https://www.python.org/dev/peps/pep-0008/) style.

Install testing dependencies with `pip install -r requirements.txt` in the project root.

Configs such as linting rule exceptions and pytest settings go in the `tox.ini` file

### Linting

Python linting is done with [flake8](http://flake8.pycqa.org/en/latest/).

Run `flake8` in the project root.  

### Unit tests

We use [pytest](https://docs.pytest.org/en/latest/) to run unit tests.

Run `pytest` in the project root.

## Support

For now, we only support Python 3, Django 2.x and Wagtail 2.x
