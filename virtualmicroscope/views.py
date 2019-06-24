#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
#
# Copyright (c) 2008-2014 University of Dundee.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Author: Aleksandra Tarkowska <A(dot)Tarkowska(at)dundee(dot)ac(dot)uk>, 2008.
#
# Version: 1.0
#

from django.views.decorators.cache import never_cache

from omero_version import omero_version

# backwords compatibility. webstart was removed in 5.2
try:
    from omeroweb.webstart.decorators import login_required, render_response
    import omeroweb.webstart.views
except ImportError:
    from omeroweb.webclient.decorators import login_required, render_response
    import omeroweb.webclient.views


@never_cache
@login_required()
@render_response()
def custom_index(request, conn=None, **kwargs):
    context = {"version": omero_version}

    active_group = (request.session.get('active_group') or
                    conn.getEventContext().groupId)
    group = conn.getObject("ExperimenterGroup", active_group)
    leaders, members = group.groupSummary()
    leaders.sort(key=lambda x: x.getOmeName() and x.getOmeName().lower())
    context["courses"] = leaders
    context['template'] = 'virtualmicroscope/start.html'
    return context


try:
    omeroweb.webstart.views.custom_index = custom_index
except AttributeError:
    omeroweb.webclient.views.custom_index = custom_index
