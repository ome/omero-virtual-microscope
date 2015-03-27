OMERO.web Virtual Microscope
============================
Virtual Microscope OMERO.web extension application

Requirements
============

* OMERO 5.1.0 or later

Development Installation
========================

Clone the repository in to your OMERO.web installation:

    $ cd components/tools/OmeroWeb/omeroweb/
    $ git clone git://github.com/openmicroscopy/virtual-microscope.git

Add virtual-microscope custom app to your installed web apps:

    $ bin/omero config append omero.web.apps '"virtual-microscope"'

NB: note that double quotes are wrapped by single quotes. Windows users will need to do

    $ bin\omero config append omero.web.apps "\"virtual-microscope\""

Redirect to your new post login page

    $ bin/omero config set omero.web.login_redirect '{"redirect": ["webindex"], "viewname": "webindex_custom"}'

Now start up OMERO.web as normal in your development environment.

Production Installation
=======================

Install the latest version of OMERO.server and OMERO.web and then:

    $ cd $OMERO_HOME/lib/python/omeroweb
    $ wget -O master.zip https://github.com/openmicroscopy/virtual-microscope/zipball/master
    $ unzip master.zip
    $ mv openmicroscopy-virtual-microscope-* virtual-microscope

Add virtual-microscope custom app to your installed web apps:

    $ bin/omero config append omero.web.apps '"virtual-microscope"'

NB: note that double quotes are wrapped by single quotes. Windows users will need to do

    $ bin\omero config append omero.web.apps "\"virtual-microscope\""

Redirect to your new post login page

    $ bin/omero config set omero.web.login_redirect '{"redirect": ["webindex"], "viewname": "webindex_custom"}'

You can then configure OMERO.web Virtual Microscope as per normal.
