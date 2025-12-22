from copy import deepcopy
from textwrap import dedent
from zest.releaser import utils

import logging
import os
import sys


# This is how towncrier imports tomli or tomllib.
if sys.version_info < (3, 11):
    import tomli as tomllib
else:
    import tomllib

logger = logging.getLogger(__name__)
TOWNCRIER_MARKER = "_towncrier_applicable"
TOWNCRIER_CONFIG_FILE = "pyproject.toml"


def _towncrier_executable():
    """Find the towncrier executable.

    We return a list, with either [path/to/towncrier] or
    [python, -m, towncrier]
    """
    # First try to find towncrier in the same directory as full/prerelease.
    # That is mostly likely to be the version that we want.
    script = sys.argv[0]
    if script == "setup.py":
        # Problem caused by 'pyroma' zest.releaser plugin.  See
        # https://github.com/collective/zestreleaser.towncrier/issues/6
        # Try the Python executable instead, which should work in case
        # zest.releaser was installed in a virtualenv.
        script = sys.executable
    releaser_path = os.path.abspath(script)
    releaser_dir = os.path.split(releaser_path)[0]
    path = os.path.join(releaser_dir, "towncrier")
    if os.path.isfile(path):
        return [path]
    # It might be a symbolic link.  Follow it and try again.
    releaser_path = os.path.realpath(releaser_path)
    releaser_dir = os.path.split(releaser_path)[0]
    path = os.path.join(releaser_dir, "towncrier")
    if os.path.isfile(path):
        return [path]
    # towncrier is in our install_requires, so it is available as module,
    # and since 18.6.0 it supports calling with 'python -m towncrier'.
    # (Note: you will want 19.2.0+ on Python 2.7.)
    return [sys.executable, "-m", "towncrier"]


def _load_config():
    with open(TOWNCRIER_CONFIG_FILE, "rb") as conffile:
        return tomllib.load(conffile)


def _is_towncrier_wanted():
    if not os.path.exists(TOWNCRIER_CONFIG_FILE):
        return
    full_config = _load_config()
    try:
        full_config["tool"]["towncrier"]
    except KeyError:
        return
    return True


def _report_newsfragments_sanity():
    """Report on the sanity of the newsfragments.

    I hope this is not too specific to the pyproject.toml config
    that I am used to.
    """
    full_config = _load_config()
    config = full_config["tool"]["towncrier"]
    if "type" in config:
        types = [entry.get("directory") for entry in config["type"]]
    else:
        # towncrier._settings._default_types seems too private to depend on,
        # so hardcopy it.
        types = ["feature", "bugfix", "doc", "removal", "misc"]
    # Where are the snippets stored?
    directory = config.get("directory")
    if not directory:
        # Look for "newsfragments" directory.
        # We could look in the config file, but I wonder if that may change,
        # so simply look for a certain directory name.
        fragment_directory = "newsfragments"
        for dirpath, dirnames, filenames in os.walk("."):
            if dirpath.startswith(os.path.join(".", ".")):
                # for example ./.git
                continue
            if fragment_directory in dirnames:
                directory = os.path.join(dirpath, fragment_directory)
                break
        if not directory:
            # Either towncrier won't work, or our logic is off.
            print("WARNING: could not find newsfragments directory for towncrier.")
            return
    problems = []
    correct = []
    for filename in os.listdir(directory):
        if filename.startswith("."):
            continue
        # filename can be like 42.bugfix or 42.bugfix.1
        filename_parts = filename.split(".")
        if 2 <= len(filename_parts) <= 3:
            # In both cases, we take item 1.
            ext = filename_parts[1]
            if ext in types:
                correct.append(filename)
                continue
        problems.append(filename)
    print(
        "Found {} towncrier newsfragments with recognized extension.".format(
            len(correct)
        )
    )
    if problems:
        print(
            dedent(
                """
            WARNING: According to the pyproject.toml file,
            towncrier accepts news snippets with these extensions:
            {}
            Problem: the {} directory contains files with other extensions,
            which will be ignored:
            {}
            """.format(
                    ", ".join(types), directory, ", ".join(problems)
                )
            )
        )
        if not utils.ask("Do you want to continue anyway?", default=False):
            sys.exit(1)
    if len(correct) == 0:
        print(
            dedent(
                """
            WARNING: No towncrier newsfragments found.
            The changelog will not contain anything interesting.
            """
            )
        )
        if not utils.ask("Do you want to continue anyway?", default=False):
            sys.exit(1)


def check_towncrier(data, check_sanity=True, do_draft=True):
    """Check if towncrier can and should be run.

    This is a zest.releaser entrypoint that is called during
    prerelease, postrelease, and bumpversion.
    Not in all cases are all checks useful, so there are some options.
    For example, postrelease should not complain that there are no
    news fragments.
    """
    if TOWNCRIER_MARKER in data:
        # We have already been called.
        return data[TOWNCRIER_MARKER]
    if not data.get("update_history", True):
        # Someone has instructed zest.releaser to not update the history,
        # and it was not us, because our marker was not set,
        # so we should not update the history either.
        logger.debug("update_history is already False, so towncrier will not be run.")
        data[TOWNCRIER_MARKER] = False
        return False
    # Check if towncrier should be applied.
    result = _is_towncrier_wanted()
    if not result:
        logger.debug("towncrier is not wanted.")
    else:
        result = _towncrier_executable()
        if result:
            logger.debug("towncrier should be run.")
            # zest.releaser should not update the history.
            # towncrier will do that.
            data["update_history"] = False
            if check_sanity:
                _report_newsfragments_sanity()
            if do_draft:
                # Do a draft.
                cmd = deepcopy(result)
                cmd.extend(
                    [
                        "build",
                        "--draft",
                        "--version",
                        data.get("new_version", "t.b.d."),
                        "--yes",
                    ]
                )
                # We would like to pass ['--package' 'package name'] as well,
                # but that is not yet in a release of towncrier.
                logger.info(
                    "Doing dry-run of towncrier to see what would be changed: %s",
                    utils.format_command(cmd),
                )
                print(utils.execute_command(cmd))
        else:
            print(
                dedent(
                    """
                According to the pyproject.toml file,
                towncrier is used to update the changelog.
                The problem is: we cannot find the towncrier executable.
                Please make sure it is on your PATH."""
                )
            )
            if not utils.ask("Do you want to continue anyway?", default=False):
                sys.exit(1)

    data[TOWNCRIER_MARKER] = result
    return result


def post_check_towncrier(data):
    """Entrypoint for postrelease."""
    return check_towncrier(data, check_sanity=False, do_draft=False)


def call_towncrier(data):
    """Entrypoint: run towncrier when available and configured."""
    # check_towncrier will either give a path to towncrier, or False.
    path = check_towncrier(data)
    if not path:
        return
    # path is a list
    cmd = deepcopy(path)
    cmd.extend(["build", "--version", data["new_version"], "--yes"])
    # We would like to pass ['--package' 'package name'] as well,
    # but that is not yet in a release of towncrier.
    logger.info("Running command to update news: %s", utils.format_command(cmd))
    print(utils.execute_command(cmd))

    # towncrier stages the changes with git,
    # which BTW means that our plugin requires git.
    logger.info("The staged git changes are:")
    print(utils.execute_command(["git", "diff", "--cached"]))
    logger.info(
        "towncrier has finished updating the history file "
        "and has staged the above changes in git."
    )
