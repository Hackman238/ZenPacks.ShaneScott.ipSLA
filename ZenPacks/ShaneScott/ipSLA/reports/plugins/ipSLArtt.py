###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2007, 2009 Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 as published by
# the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/
#
###########################################################################

import Globals
from Products.ZenReports.AliasPlugin import AliasPlugin, Column, \
                                            RRDColumnHandler, \
                                            PythonColumnHandler

class ipSLArtt( AliasPlugin ):
    """
    ipSLA round trip time report
    """

    def getComponentPath(self):
        return 'ipSLAs'

    def _getComponents(self, device, componentPath):
        components=[]
        try:
            for s in device.ipSLAs():
                components.append(s)
        except AttributeError:
            pass
        return components

    def getColumns(self):
        return [
                Column('deviceName', PythonColumnHandler( 'device.titleOrId()' )),
                Column('SLA', PythonColumnHandler( 'component.name()' )),
                Column('RTT', RRDColumnHandler( 'rttMonLatestRttOperCompletionTime' )),
                ]
