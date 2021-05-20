from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

INSTALL_REQUIRES = [
    'Wagtail>=2.0',
]


setup(
    name="wagtail-nhsuk-frontend",
    version="0.8.0",
    description="NHSUK Frontend Styles for Wagtail",
    author="Mike Monteith",
    author_email="<mike.monteith@nhs.net>",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nhsuk/wagtail-nhsuk-frontend",
    install_requires=INSTALL_REQUIRES,
    packages=find_packages(),
    include_package_data=True,
)
