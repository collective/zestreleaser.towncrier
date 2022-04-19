# -*- coding: utf-8 -*-
"""Installer for the zestreleaser.towncrier package."""

from setuptools import find_packages, setup

LITERAL_TOML = """
``pyproject.toml`` example
--------------------------

``towncrier`` needs a configured ``pyproject.toml`` file in the root of the package, next to the ``setup.py``.
For reference, here is the literal ``pyproject.toml`` file from ``zestreleaser.towncrier``::

"""
with open("pyproject.toml") as toml:
    for line in toml.readlines():
        LITERAL_TOML += "  " + line

long_description = "\n\n".join(
    [
        open("README.rst").read(),
        LITERAL_TOML,
        open("CONTRIBUTORS.rst").read(),
        open("CHANGES.rst").read(),
    ]
)


setup(
    name="zestreleaser.towncrier",
    version="1.3.0",
    description="zest.releaser plugin to call towncrier",
    long_description=long_description,
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="Python Plone",
    author="Maurits van Rees",
    author_email="m.van.rees@zestsoftware.nl",
    url="https://pypi.org/project/zestreleaser.towncrier",
    license="GPL",
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["zestreleaser"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "setuptools",
        "toml; python_version < '3.6'",
        "tomli; python_version >= '3.6'",
        "towncrier>=19.9.0",
        "zest.releaser>=6.17.0",
    ],
    entry_points={
        "zest.releaser.bumpversion.before": [
            # If towncrier is configured for this project,
            # the history should not be changed.
            "check_towncrier = zestreleaser.towncrier:check_towncrier",
        ],
        "zest.releaser.prereleaser.middle": [
            # Call towncrier to update the changelog with newsfragments:
            "call_towncrier = zestreleaser.towncrier:call_towncrier",
        ],
        "zest.releaser.prereleaser.before": [
            # Check if towncrier is available and configured:
            "check_towncrier = zestreleaser.towncrier:check_towncrier",
        ],
        "zest.releaser.postreleaser.before": [
            # We only need to check if towncrier is available and
            # configured for this project.
            # Then the history should not be changed.
            "check_towncrier = zestreleaser.towncrier:post_check_towncrier",
        ],
    },
)
