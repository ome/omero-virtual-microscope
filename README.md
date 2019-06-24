OMERO.web Virtual Microscope
============================
Virtual Microscope OMERO.web extension application

Requirements
============

* OMERO 5.4.0 or later

Installation
============

    $ pip install https://github.com/ome/virtual-microscope/archive/master.zip

Add virtual-microscope custom app to your installed web apps:

    $ bin/omero config append omero.web.apps '"virtualmicroscope"'

NB: note that double quotes are wrapped by single quotes. Windows users will need to do

    $ bin\omero config append omero.web.apps "\"virtualmicroscope\""

Redirect to post-login page

    $ bin/omero config set omero.web.login_redirect '{"redirect": ["webindex"], "viewname": "webindex_custom", "query_string": "", "args": []}'

Now start up OMERO.web as normal.
