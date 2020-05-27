from setuptools import setup, find_packages
from configparser import ConfigParser

version = "0.1.dev0"

long_description = "\n\n".join([open("README.md").read(), open("CHANGES.md").read()])


def parse_pipfile():
    """Reads package requirements from Pipfile."""
    cfg = ConfigParser()
    cfg.read('Pipfile')
    dev_packages = [p.strip('"') for p in cfg['dev-packages']]
    relevant_packages = [
        p.strip('"') for p in cfg['packages'] if "cookiecutter-demo" not in p
    ]
    return relevant_packages, dev_packages


# We use Pipenv. Please set requirements in Pipfile.
install_requirements, tests_requirements = parse_pipfile()


setup(
    name="cookiecutter-demo",
    version=version,
    description="Demo van cookiecutter-python-base van PDOK",
    long_description=long_description,
    # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=["Programming Language :: Python :: 3"],
    keywords=["cookiecutter-demo"],
    author="Roel van den Berg",
    author_email="roel.vandenberg@kadaster.nl",
    url="https://github.com/PDOK/cookiecutter-demo",
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requirements,
    tests_require=tests_requirements,
    entry_points={
        "console_scripts": [
            "demo-cookiecutter = cookiecutter_demo.cli:cookiecutter_demo_command"
        ]
    },
)
