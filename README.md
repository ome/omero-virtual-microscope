OMERO.web Virtual Microscope
============================
Virtual Microscope OMERO.web extension application

Requirements
============

* OMERO 5.1.0 or later

Development Installation
========================

Clone the repository in to your OMERO.web installation:

    cd components/tools/OmeroWeb/omeroweb/
    git clone git://github.com/openmicroscopy/virtual-microscope.git
    path/to/bin/omero config set omero.web.apps '["virtual-microscope"]'

Now start up OMERO.web as normal in your development environment.

Production Installation
=======================

Install the latest version of OMERO.server and OMERO.web and then:

    cd $OMERO_HOME/lib/python/omeroweb
    wget -O master.zip https://github.com/openmicroscopy/virtual-microscope/zipball/master
    unzip master.zip
    mv openmicroscopy-virtual-microscope-* virtual-microscope
    path/to/bin/omero config set omero.web.apps '["virtual-microscope"]'

You can then configure OMERO.web Virtual Microscope as per normal.
