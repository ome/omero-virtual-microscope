OMERO.web Virtual Microscope
============================
Virtual Microscope OMERO.web extension application

Requirements
============

* OMERO 5.1.0 or later

Installation
============

Clone

    $ git clone git://github.com/openmicroscopy/virtual-microscope.git virtual-microscope

or download

    $ wget -O master.zip https://github.com/openmicroscopy/virtual-microscope/zipball/master
    $ unzip master.zip
    $ mv openmicroscopy-virtual-microscope-* virtual-microscope

Add virtual-microscope to PYTHONPATH:

    $ export PYTHONPATH=/path/to/virtual-microscope:$PYTHONPATH

Add virtual-microscope custom app to your installed web apps:

    $ bin/omero config append omero.web.apps '"virtualmicroscope"'

NB: note that double quotes are wrapped by single quotes. Windows users will need to do

    $ bin\omero config append omero.web.apps "\"virtualmicroscope\""

Redirect to post-login page

    $ bin/omero config set omero.web.login_redirect '{"redirect": ["webindex"], "viewname": "webindex_custom", "query_string": "", "args": []}'

Now start up OMERO.web as normal.
