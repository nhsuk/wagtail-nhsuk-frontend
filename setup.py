from setuptools import setup, find_packages

INSTALL_REQUIRES = [
    'Wagtail>=2.0',
]

TESTING_REQUIRES = [

]

setup(
    name="wagtail-nhs-style",
    version="0.0.1",
    description="NHS Frontend Styles for Wagtail",
    author="Mike Monteith",
    author_email="<mike.monteith@nhs.net>",
    install_requires=INSTALL_REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    extras_require={'testing': TESTING_REQUIRES},
)
