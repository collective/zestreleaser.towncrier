Changelog
=========

.. NOTE: You should *NOT* be adding new change log entries to this file, this
         file is managed by towncrier. You *may* edit previous change logs to
         fix problems like typo corrections or such.

         To add a new change log entry, please see the notes from the ``pip`` project at
             https://pip.pypa.io/en/latest/development/#adding-a-news-entry

.. towncrier release notes start

2.0.0 (2025-12-29)
------------------

Breaking changes:


- Require at least Python 3.10.  [maurits]
- Use native (implicit) namespace.  [maurits]


New features:


- Call ``towncrier check`` instead of doing those checks ourselves.  [maurits] (`Issue #29 <https://github.com/collective/zestreleaser.towncrier/issues/29>`_)


Bug fixes:


- Also look for ``towncrier.toml``, next to ``pyproject.toml``.
  ``towncrier.toml`` is tried first.
  [maurits] (`Issue #27 <https://github.com/collective/zestreleaser.towncrier/issues/27>`_)


1.3.0 (2022-04-19)
------------------

New features:


- Use the ``build`` subcommand for ``towncrier`` to build the changelog.
  Fixes compatibility with ``towncrier`` 21.9.0 or later.
  Requires ``towncrier`` 19.9.0 or later.
  [mcflugen] (`Issue #22 <https://github.com/collective/zestreleaser.towncrier/issues/22>`_)
- For parsing, use ``tomli`` when on Python 3, ``toml`` on Python 2.
  Same as ``towncrier`` did until recently.
  [maurits] (`Issue #23 <https://github.com/collective/zestreleaser.towncrier/issues/23>`_)


1.2.0 (2019-03-05)
------------------

New features:


- Use 'python -m towncrier' when the script is not easily findable.
  Still check the directory of the fullrelease script first.
  No longer check the PATH.
  [maurits] (`Issue #17 <https://github.com/collective/zestreleaser.towncrier/issues/17>`_)


Bug fixes:


- Do not run sanity checks or run draft during postrelease.  [maurits] (`Issue #16 <https://github.com/collective/zestreleaser.towncrier/issues/16>`_)


1.1.0 (2019-03-05)
------------------

New features:


- Rerelease 1.0.3 as 1.1.0, as it contains new features. (`Issue #9 <https://github.com/collective/zestreleaser.towncrier/issues/9>`_)


1.0.3 (2019-03-05)
------------------

New features:


- Report on sanity of newsfragments: do they have the correct extensions?
  Is at least one found?
  Show dry-run (draft) of what towncrier would do.
  [maurits] (`Issue #9 <https://github.com/collective/zestreleaser.towncrier/issues/9>`_)
- Handle multiple news entries per issue/type pair.  [maurits] (`Issue #14 <https://github.com/collective/zestreleaser.towncrier/issues/14>`_)


1.0.2 (2019-03-04)
------------------

Bug fixes:


- Fixed finding towncrier when sys.argv is messed up.  [maurits] (`Issue #6 <https://github.com/collective/zestreleaser.towncrier/issues/6>`_)


1.0.1 (2019-02-20)
------------------

Bug fixes:


- Tell bumpversion to not update the history. [maurits] (`Issue #10
  <https://github.com/collective/zestreleaser.towncrier/issues/10>`_)


1.0.0 (2019-02-06)
------------------

New features:


- Warn and ask when towncrier is wanted but not found. [maurits] (`Issue #7
  <https://github.com/collective/zestreleaser.towncrier/issues/7>`_)


1.0.0b3 (2018-05-17)
--------------------

New features:


- Require towncrier 18.5.0 so we don't need a package name in the config.
  [maurits] (`Issue #3
  <https://github.com/collective/zestreleaser.towncrier/issues/3>`_)


Bug fixes:


- First look for ``towncrier`` next to the ``full/prerelease`` script. Then
  fall back to looking on the ``PATH``. [maurits] (`Issue #4
  <https://github.com/collective/zestreleaser.towncrier/issues/4>`_)


1.0.0b2 (2018-05-16)
--------------------

Bug fixes:


- Do not fail when pyproject.toml file is not there. [maurits] (`Issue #2
  <https://github.com/collective/zestreleaser.towncrier/issues/2>`_)


1.0.0b1 (2018-05-15)
--------------------

New features:


- First release. [maurits] (`Issue #1
  <https://github.com/collective/zestreleaser.towncrier/issues/1>`_)
