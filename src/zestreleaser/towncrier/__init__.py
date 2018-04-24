# -*- coding: utf-8 -*-
from zest.releaser import utils

import distutils.spawn
import logging
import os
import sys
import toml


logger = logging.getLogger(__name__)
TOWNCRIER_MARKER = '_towncrier_applicable'
TOWNCRIER_CONFIG_FILE = 'pyproject.toml'


def _towncrier_executable():
    # Find the towncrier executable.
    # First option is taken from
    # https://stackoverflow.com/questions/377017
    path = distutils.spawn.find_executable('towncrier')
    if path:
        return path
    releaser_path = os.path.abspath(sys.argv[0])
    releaser_dir = os.path.split(releaser_path)[0]
    path = os.path.join(releaser_dir, 'towncrier')
    if os.path.isfile(path):
        return path
    # It might be a symbolic link.  Follow it and try again.
    releaser_path = os.path.realpath(releaser_path)
    releaser_dir = os.path.split(releaser_path)[0]
    path = os.path.join(releaser_dir, 'towncrier')
    if os.path.isfile(path):
        return path
    return


def _load_config():
    with open(TOWNCRIER_CONFIG_FILE, 'r') as conffile:
        full_config = toml.load(conffile)
    try:
        config = full_config['tool']['towncrier']
    except KeyError:
        return
    # Currently we need 'package' in the config.
    if 'package' not in config:
        logger.error(
            "The [tool.towncrier] section of %s "
            "has no required 'package' key.", TOWNCRIER_CONFIG_FILE)
        return
    return True


def _is_towncrier_enabled():
    # First check if the towncrier tool is available.
    # towncrier might be on the PATH but not importable,
    # or the other way around.
    if not _towncrier_executable():
        return False
    # Read pyproject.toml with the toml package.
    if not _load_config():
        return False
    return True


def check_towncrier(data):
    if TOWNCRIER_MARKER in data:
        # We have already been called.
        return data[TOWNCRIER_MARKER]
    if not data['update_history']:
        # Someone has instructed zest.releaser to not update the history,
        # and it was not us, because our marker was not set,
        # so we should not update the history either.
        logger.debug(
            'update_history is already False, so towncrier will not be run.')
        data[TOWNCRIER_MARKER] = False
        return False
    # Check if towncrier should be applied.
    result = _is_towncrier_enabled()
    if result:
        logger.debug('towncrier should be run.')
        # zest.releaser should not update the history.
        # towncrier will do that.
        data['update_history'] = False
    else:
        logger.debug('towncrier is not available or not configured.')
    data[TOWNCRIER_MARKER] = result
    return result


def call_towncrier(data):
    """Entrypoint: run towncrier when available and configured."""
    if not check_towncrier(data):
        return
    path = _towncrier_executable()
    cmd = [path, '--version', data['new_version'], '--yes']
    # We would like to pass ['--package' 'package name'] as well,
    # but that is not yet in a release of towncrier.
    logger.info(
        'Running command to update news: %s', utils.format_command(cmd))
    print(utils.execute_command(cmd))

    # towncrier stages the changes with git,
    # which BTW means that our plugin requires git.
    logger.info('The staged git changes are:')
    print(utils.execute_command(['git', 'diff', '--cached']))
    logger.info(
        'towncrier has finished updating the history file '
        'and has staged the above changes in git.')
