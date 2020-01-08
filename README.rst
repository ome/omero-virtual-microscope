OMERO.web Virtual Microscope
============================
Virtual Microscope OMERO.web extension application

Requirements
============

* OMERO.web 5.6.0 or later

Installation
============

    $ pip install omero-virtual-microscope

Add virtual-microscope custom app to your installed web apps:

    $ omero config append omero.web.apps '"virtualmicroscope"'

N.B.: note that double quotes are wrapped by single quotes. Windows users will need to do

    $ omero config append omero.web.apps "\"virtualmicroscope\""

Redirect to post-login page

    $ omero config set omero.web.login_redirect '{"redirect": ["webindex"], "viewname": "webindex_custom"}'

Now start up OMERO.web as normal.
