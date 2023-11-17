from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

INSTALL_REQUIRES = [
    "Wagtail>=4.1",
]

TESTING_REQUIRES = [
    "beautifulsoup4==4.8.2",
    "Django>=3.2",
    "pytest==6.2.5",
    "pytest-django==4.5.2",
    "pytest-pythonpath==0.7.4",
]

LINTING_REQUIRES = [
    "flake8>=5.0.4,<5.1",
]


setup(
    name="wagtail-nhsuk-frontend",
    version="1.5.3",
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
