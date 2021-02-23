# Contributing

## Running the application locally

### Requirements: 

To run the Wagtail CMS locally you'll need:

- [Python 3.x](https://www.python.org/downloads/)
- [Pip](https://pypi.org/project/pip/) - if you have Python version 3.4 or later, PIP is included by default.

> Type `python --version` to check if Python is installed. This should print a version number like "Python 3.7.3".

> Type `pip --version` to check if Pip is installed. This should print a version number and folder path like "pip 19.0.3 from /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pip (python 3.7)"

### 1. Clone the repository

```
git clone https://github.com/nhsuk/wagtail-nhsuk-frontend.git wagtail-nhsuk-frontend
```

### 2. Create a virtual environment

Whilst in the `wagtail-nhsuk-frontend` directory:

```
pipenv shell
```

### 3. Build the application CSS

```
python3 setup.py build
```

### 4. Install dependencies

```
cd testapp
```

```
pip3 install -r requirements.txt
```

### 5. Run database migrations

```
python3 manage.py migrate
```

### 6. Create Wagtail admin user

```
python3 manage.py createsuperuser
```

### 7. Start a local server 

```
python3 manage.py runserver 8080
```

The application will be available at http://localhost:8080 and the admin panel can be found at http://localhost:8080/admin

## Test data

To install the test fixture, make sure you have an empty but fully migrated database.

Run `python3 manage.py loaddata testdata.json` and rerun the local server `python3 manage.py runserver 8080` 

You should now have sample content pages in your wagtail installation.

The default login is username="admin" and password="password123"

## Develop/Contribute using Gitpod
[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/nhsuk/wagtail-nhsuk-frontend)

Opening this project in gitpod (click the button above), it will run all the scripts above for you and run the tests. You can then start developing to make your contibution.

Just start the local server... from the testapp folder run

```
python manage.py runserver 0:8000
```

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
