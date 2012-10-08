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

class ipSLApktloss( AliasPlugin ):
    """
    ipSLA packet loss report
    """

    def getComponentPath(self):
        return 'ipSLAs'

    def _getComponents(self, device, componentPath):
        components=[]
        try:
            for s in device.ipSLAs():
                if s.rttMonCtrlAdminRttType == "Jitter":
                    components.append(s)
        except AttributeError:
            pass
        return components

    def getColumns(self):
        return [
                Column('deviceName', PythonColumnHandler( 'device.titleOrId()' )),
                Column('SLA', PythonColumnHandler( 'component.name()' )),
                Column('droppedPkts', RRDColumnHandler( 'rttMonLatestJitterOperPacketLossSD' )),
                Column('sentPkts', RRDColumnHandler( 'rttMonEchoAdminNumPackets' )),
                ]

    def getCompositeColumns(self):
        return [
                Column('percentLoss', PythonColumnHandler('float(droppedPkts)/float(sentPkts)'))
                ]
