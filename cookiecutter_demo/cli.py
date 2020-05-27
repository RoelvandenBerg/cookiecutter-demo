# -*- coding: utf-8 -*-
"""TODO Docstring."""
import logging
import sys

import click
import click_log

# Setup logging before package imports.
logger = logging.getLogger(__name__)
click_log.basic_config(logger)

from cookiecutter_demo.core import main
from cookiecutter_demo.error import AppError


@click.group()
def cli():
    pass


@cli.command(name="cookiecutter_demo")
@click_log.simple_verbosity_option(logger)
def cookiecutter_demo_command():
    """
    TODO Docstring.
    """
    try:
        main()
    except AppError:
        logger.exception("cookiecutter_demo failed:")
        sys.exit(1)


if __name__ == "__main__":
    cli()
