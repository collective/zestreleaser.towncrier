Changelog
=========

.. NOTE: You should *NOT* be adding new change log entries to this file, this
         file is managed by towncrier. You *may* edit previous change logs to
         fix problems like typo corrections or such.

         To add a new change log entry, please see the notes from the ``pip`` project at
             https://pip.pypa.io/en/latest/development/#adding-a-news-entry

.. towncrier release notes start

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
