.. image:: https://github.com/ome/omero-virtual-microscope/workflows/OMERO/badge.svg
    :target: https://github.com/ome/omero-virtual-microscope/actions

.. image:: https://badge.fury.io/py/omero-virtual-microscope.svg
    :target: https://badge.fury.io/py/omero-virtual-microscope

OMERO.web Virtual Microscope
============================
Virtual Microscope OMERO.web extension application

Requirements
------------

* OMERO.web 5.6.0 or later

Installation
------------

    $ pip install omero-virtual-microscope

Add virtual-microscope custom app to your installed web apps:

    $ omero config append omero.web.apps '"virtualmicroscope"'

N.B.: note that double quotes are wrapped by single quotes. Windows users will need to do

    $ omero config append omero.web.apps "\"virtualmicroscope\""

Redirect to post-login page

    $ omero config set omero.web.login_redirect '{"redirect": ["webindex"], "viewname": "webindex_custom"}'

Now start up OMERO.web as normal.

Release process
---------------

This repository uses `bump2version <https://pypi.org/project/bump2version/>`_ to manage version numbers.
To tag a release run::

    $ bumpversion release

This will remove the ``.dev0`` suffix from the current version, commit, and tag the release.

To switch back to a development version run::

    $ bumpversion --no-tag [major|minor|patch]

specifying ``major``, ``minor`` or ``patch`` depending on whether the development branch will be a `major, minor or patch release <https://semver.org/>`_. This will also add the ``.dev0`` suffix.

Remember to ``git push`` all commits and tags.

License
-------

This project, similar to many Open Microscopy Environment (OME) projects, is
licensed under the terms of the GNU General Public License (GPL) v2 or later.

Copyright
---------

2019-2020, The Open Microscopy Environment
