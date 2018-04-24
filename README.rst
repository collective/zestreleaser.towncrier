.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

zestreleaser.towncrier
======================

This calls `towncrier <https://github.com/hawkowl/towncrier>`_ when releasing a package with `zest.releaser <http://zestreleaser.readthedocs.io/en/latest/>`_.
``towncrier`` updates your history file (like ``CHANGES.rst``) based on news snippets.
This is for example `used by pip <https://pip.pypa.io/en/latest/development/#adding-a-news-entry>`_.

The plugin will call ``towncrier --version <package version> --yes``.
You can get a preview of the result yourself by calling ``towncrier --version 1.2.3 --draft``.

The ``towncrier`` command should be on your ``PATH``.
The plugin can also find it when it is in the same directory as the ``fullrelease`` script (or ``prerelease/postrelease``).


Installation
------------

Install ``zestreleaser.towncrier`` with ``pip``::

    $ pip install zestreleaser.towncrier

Then you can run ``fullrelease`` like you would normally do when releasing a package.


Contribute
----------

- Issue Tracker: https://github.com/collective/zestreleaser.towncrier/issues
- Source Code: https://github.com/collective/zestreleaser.towncrier


Support
-------

If you are having problems, please let us know by filing an `issue <https://github.com/collective/zestreleaser.towncrier/issues>`_.


License
-------

The project is licensed under the GPL.
