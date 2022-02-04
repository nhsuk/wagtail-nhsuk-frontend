from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

INSTALL_REQUIRES = [
    'Wagtail>=2.0',
]

TESTING_REQUIRES = [
    "beautifulsoup4==4.8.2",
    "Django>=3.1,<3.2",
    "pytest==4.3.0",
    "pytest-django==3.4.7",
    "pytest-pythonpath==0.7.3",
]

LINTING_REQUIRES = [
    "flake8==3.7.5",
]


setup(
    name="wagtail-nhsuk-frontend",
    version="1.2.3",
    description="NHSUK Frontend Styles for Wagtail",
    author="Mike Monteith",
    author_email="<mike.monteith@nhs.net>",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nhsuk/wagtail-nhsuk-frontend",
    install_requires=INSTALL_REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    extras_require={"testing": TESTING_REQUIRES, "linting": LINTING_REQUIRES},
)
