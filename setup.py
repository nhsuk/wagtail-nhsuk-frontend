from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

INSTALL_REQUIRES = [
    'Wagtail>=5.2',
]

TESTING_REQUIRES = [
    "beautifulsoup4==4.12.3",
    "Django>=4.2",
    "pytest==8.2.1",
    "pytest-django==4.8.0",
]

LINTING_REQUIRES = [
    "flake8>=5.0.4,<7.0.0",
]


setup(
    name="wagtail-nhsuk-frontend",
    version="1.6.0",
    description="NHSUK Frontend Styles for Wagtail",
    author="Brad Morton",
    author_email="<bradley.morton1@nhs.net>",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nhsuk/wagtail-nhsuk-frontend",
    install_requires=INSTALL_REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    extras_require={"testing": TESTING_REQUIRES, "linting": LINTING_REQUIRES},
)
