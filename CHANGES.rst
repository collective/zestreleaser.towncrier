Changelog
=========

.. NOTE: You should *NOT* be adding new change log entries to this file, this
         file is managed by towncrier. You *may* edit previous change logs to
         fix problems like typo corrections or such.

         To add a new change log entry, please see the notes from the ``pip`` project at
             https://pip.pypa.io/en/latest/development/#adding-a-news-entry

.. towncrier release notes start

1.0.4 (2019-03-05)
------------------

No significant changes.


1.0.4 (2019-03-05)
------------------

Bug fixes:


- Rerelease of 1.0.2 as 1.0.4.
  The 1.0.3 contained new features, so should have been a 1.1.0 release.
  [maurits]


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
