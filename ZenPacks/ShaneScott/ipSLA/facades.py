import os
import logging
log = logging.getLogger('zen.SLAFacade')

from zope.interface import implements

from Products.Zuul.facades import ZuulFacade
from Products.Zuul.utils import ZuulMessageFactory as _t

from .interfaces import ISLAFacade

SLA_DEVICE_PATH = "/Devices/Network/IPSLA"


class SLAFacade(ZuulFacade):
    implements(ISLAFacade)

    def manage_delSLAs(self, rttIndex, deviceIp, community):
        """Delete a SLA on a host"""
        cmd="""
               snmpset -v2c -c """ + community + """ """ + deviceIp + """  \
               .1.3.6.1.4.1.9.9.42.1.2.1.1.9.""" + str(rttIndex) + """ i 6
               """

        os.system(str(cmd))
        return True


    def manage_writeMemSLAs(self, deviceIp, community):
        """Write mem on a host"""
        cmd="""
               snmpset -v2c -c """ + community + """ """ + deviceIp + """  \
               .1.3.6.1.4.1.9.2.1.54.0 i 1
               """

        os.system(str(cmd))
        return True


    def manage_addTcpSLAs(self, newId, rttIndex, deviceIp, community, rttMonEchoAdminTargetAddress, rttMonEchoAdminTargetPort, rttMonScheduleAdminRttStartTime=1, rttMonCtrlAdminOwner="zenoss"):
        """Add a SLA to this SLA host"""
        tag = str(newId)
        cmd="""
               snmpset -v2c -c """ + community + """ """ + deviceIp + """  \
               .1.3.6.1.4.1.9.9.42.1.2.1.1.9.""" + str(rttIndex) + """ i 4 \
               .1.3.6.1.4.1.9.9.42.1.2.1.1.4.""" + str(rttIndex) + """ i 6 \
               .1.3.6.1.4.1.9.9.42.1.2.2.1.1.""" + str(rttIndex) + """ i 24 \
               .1.3.6.1.4.1.9.9.42.1.2.1.1.3.""" + str(rttIndex) + """ s '""" + newId + """' \
               .1.3.6.1.4.1.9.9.42.1.2.1.1.2.""" + str(rttIndex) + """ s '""" + rttMonCtrlAdminOwner + """' \
               .1.3.6.1.4.1.9.9.42.1.2.2.1.2.""" + str(rttIndex) + """ x '""" + toHex(rttMonEchoAdminTargetAddress) + """' \
               .1.3.6.1.4.1.9.9.42.1.2.2.1.5.""" + str(rttIndex) + """ i """ + str(rttMonEchoAdminTargetPort) + """ \
               .1.3.6.1.4.1.9.9.42.1.2.5.1.2.""" + str(rttIndex) + """ t """ + str(rttMonScheduleAdminRttStartTime) + """
               """
        log.info("SLA Add cmd %s", cmd)

        os.system(str(cmd))
        return True


    def manage_addJitterSLAs(self, newId, rttIndex, deviceIp, community, rttMonEchoAdminTargetAddress, rttMonEchoAdminTargetPort, rttMonEchoAdminInterval=60, rttMonEchoAdminNumPackets=100, rttMonScheduleAdminRttStartTime=1, rttMonCtrlAdminOwner="zenoss"):
        """Add a SLA to this SLA host"""
        tag = str(newId)
        cmd="""
               snmpset -v2c -c """ + community + """ """ + deviceIp + """  \
               .1.3.6.1.4.1.9.9.42.1.2.1.1.4.""" + str(rttIndex) + """ i 9 \
               .1.3.6.1.4.1.9.9.42.1.2.1.1.3.""" + str(rttIndex) + """ s '""" + newId + """' \
               .1.3.6.1.4.1.9.9.42.1.2.1.1.2.""" + str(rttIndex) + """ s '""" + rttMonCtrlAdminOwner + """' \
               .1.3.6.1.4.1.9.9.42.1.2.2.1.1.""" + str(rttIndex) + """ i 27 \
               .1.3.6.1.4.1.9.9.42.1.2.2.1.2.""" + str(rttIndex) + """ x '""" + toHex(rttMonEchoAdminTargetAddress) + """' \
               .1.3.6.1.4.1.9.9.42.1.2.2.1.5.""" + str(rttIndex) + """ i """ + str(rttMonEchoAdminTargetPort) + """ \
               .1.3.6.1.4.1.9.9.42.1.2.2.1.17.""" + str(rttIndex) + """ i """ + str(rttMonEchoAdminInterval) + """ \
               .1.3.6.1.4.1.9.9.42.1.2.2.1.18.""" + str(rttIndex) + """ i """ + str(rttMonEchoAdminNumPackets) + """ \
               .1.3.6.1.4.1.9.9.42.1.2.5.1.2.""" + str(rttIndex) + """ t """ + str(rttMonScheduleAdminRttStartTime) + """ \
               .1.3.6.1.4.1.9.9.42.1.2.1.1.9.""" + str(rttIndex) + """ i 4
               """
        log.info("SLA Add cmd %s", cmd)

        os.system(str(cmd))
        return True


    def manage_addDnsSLAs(self, newId, rttIndex, deviceIp, community, rttMonEchoAdminNameServer, rttMonEchoAdminTargetAddressString, rttMonScheduleAdminRttStartTime=1, rttMonCtrlAdminOwner="zenoss"):
        """Add a SLA to this SLA host"""
        tag = str(newId)
        cmd="""
               snmpset -v2c -c """ + community + """ """ + deviceIp + """  \
               .1.3.6.1.4.1.9.9.42.1.2.1.1.4.""" + str(rttIndex) + """ i 8 \
               .1.3.6.1.4.1.9.9.42.1.2.1.1.3.""" + str(rttIndex) + """ s '""" + newId + """' \
               .1.3.6.1.4.1.9.9.42.1.2.1.1.2.""" + str(rttIndex) + """ s '""" + rttMonCtrlAdminOwner + """' \
               .1.3.6.1.4.1.9.9.42.1.2.2.1.1.""" + str(rttIndex) + """ i 26 \
               .1.3.6.1.4.1.9.9.42.1.2.2.1.11.""" + str(rttIndex) + """ s '""" + rttMonEchoAdminTargetAddressString + """' \
               .1.3.6.1.4.1.9.9.42.1.2.2.1.12.""" + str(rttIndex) + """ s '""" + rttMonEchoAdminNameServer + """' \
               .1.3.6.1.4.1.9.9.42.1.2.5.1.2.""" + str(rttIndex) + """ t """ + str(rttMonScheduleAdminRttStartTime) + """ \
               .1.3.6.1.4.1.9.9.42.1.2.1.1.9.""" + str(rttIndex) + """ i 4
               """
        log.info("SLA Add cmd %s", cmd)

        os.system(str(cmd))
        return True


    def manage_addDhcpSLAs(self, newId, rttIndex, deviceIp, community, rttMonScheduleAdminRttStartTime=1, rttMonCtrlAdminOwner="zenoss"):
        """Add a SLA to this SLA host"""
        tag = str(newId)
        cmd="""
               snmpset -v2c -c """ + community + """ """ + deviceIp + """  \
               .1.3.6.1.4.1.9.9.42.1.2.1.1.4.""" + str(rttIndex) + """ i 11 \
               .1.3.6.1.4.1.9.9.42.1.2.1.1.3.""" + str(rttIndex) + """ s '""" + newId + """' \
               .1.3.6.1.4.1.9.9.42.1.2.1.1.2.""" + str(rttIndex) + """ s '""" + rttMonCtrlAdminOwner + """' \
               .1.3.6.1.4.1.9.9.42.1.2.2.1.1.""" + str(rttIndex) + """ i 29 \
               .1.3.6.1.4.1.9.9.42.1.2.2.1.13.""" + str(rttIndex) + """ i 2 \
               .1.3.6.1.4.1.9.9.42.1.2.5.1.2.""" + str(rttIndex) + """ t """ + str(rttMonScheduleAdminRttStartTime) + """ \
               .1.3.6.1.4.1.9.9.42.1.2.1.1.9.""" + str(rttIndex) + """ i 4
               """
        log.info("SLA Add cmd %s", cmd)

        os.system(str(cmd))
        return True

    def manage_addEchoSLAs(self, newId, rttIndex, deviceIp, community, rttMonEchoAdminTargetAddress, rttMonScheduleAdminRttStartTime=1, rttMonCtrlAdminFrequency=60, rttMonCtrlAdminOwner="zenoss", rttMonCtrlAdminThreshold=5000, rttMonCtrlAdminTimeout=5):
        """Add a SLA to this SLA host"""
        tag = str(newId)
        cmd="""
               snmpset -v2c -c """ + community + """ """ + deviceIp + """  \
               .1.3.6.1.4.1.9.9.42.1.2.1.1.4.""" + str(rttIndex) + """ i 1 \
               .1.3.6.1.4.1.9.9.42.1.2.1.1.3.""" + str(rttIndex) + """ s '""" + newId + """' \
               .1.3.6.1.4.1.9.9.42.1.2.1.1.2.""" + str(rttIndex) + """ s '""" + rttMonCtrlAdminOwner + """' \
               .1.3.6.1.4.1.9.9.42.1.2.2.1.1.""" + str(rttIndex) + """ i 2 \
               .1.3.6.1.4.1.9.9.42.1.2.2.1.2.""" + str(rttIndex) + """ x '""" + toHex(rttMonEchoAdminTargetAddress) + """' \
               .1.3.6.1.4.1.9.9.42.1.2.1.1.5.""" + str(rttIndex) + """ i """ + str(rttMonCtrlAdminThreshold) + """ \
               .1.3.6.1.4.1.9.9.42.1.2.1.1.6.""" + str(rttIndex) + """ i """ + str(rttMonCtrlAdminFrequency) + """ \
               .1.3.6.1.4.1.9.9.42.1.2.1.1.7.""" + str(rttIndex) + """ i """ + str(rttMonCtrlAdminTimeout) + """ \
               .1.3.6.1.4.1.9.9.42.1.2.2.1.13.""" + str(rttIndex) + """ i 2 \
               .1.3.6.1.4.1.9.9.42.1.2.5.1.2.""" + str(rttIndex) + """ t """ + str(rttMonScheduleAdminRttStartTime) + """ \
               .1.3.6.1.4.1.9.9.42.1.2.1.1.9.""" + str(rttIndex) + """ i 4
               """
        log.info("SLA Add cmd %s", cmd)

        os.system(str(cmd))
        return True


    def manage_addHttpSLAs(self, newId, rttIndex, deviceIp, community, rttMonEchoAdminURL, rttMonScheduleAdminRttStartTime=1, rttMonCtrlAdminFrequency=60, rttMonCtrlAdminOwner="zenoss", rttMonCtrlAdminThreshold=5000, rttMonCtrlAdminTimeout=5):
        """Add a SLA to this SLA host"""
        tag = str(newId)
        cmd="""
               snmpset -v2c -c """ + community + """ """ + deviceIp + """  \
               .1.3.6.1.4.1.9.9.42.1.2.1.1.4.""" + str(rttIndex) + """ i 7 \
               .1.3.6.1.4.1.9.9.42.1.2.1.1.3.""" + str(rttIndex) + """ s '""" + newId + """' \
               .1.3.6.1.4.1.9.9.42.1.2.1.1.2.""" + str(rttIndex) + """ s '""" + rttMonCtrlAdminOwner + """' \
               .1.3.6.1.4.1.9.9.42.1.2.1.1.5.""" + str(rttIndex) + """ i """ + str(rttMonCtrlAdminThreshold) + """ \
               .1.3.6.1.4.1.9.9.42.1.2.1.1.6.""" + str(rttIndex) + """ i """ + str(rttMonCtrlAdminFrequency) + """ \
               .1.3.6.1.4.1.9.9.42.1.2.1.1.7.""" + str(rttIndex) + """ i """ + str(rttMonCtrlAdminTimeout) + """ \
               .1.3.6.1.4.1.9.9.42.1.2.2.1.1.""" + str(rttIndex) + """ i 25 \
               .1.3.6.1.4.1.9.9.42.1.2.2.1.13.""" + str(rttIndex) + """ i 2 \
               .1.3.6.1.4.1.9.9.42.1.2.5.1.2.""" + str(rttIndex) + """ t """ + str(rttMonScheduleAdminRttStartTime) + """ \
               .1.3.6.1.4.1.9.9.42.1.2.2.1.15.""" + str(rttIndex) + """ s '""" + rttMonEchoAdminURL + """' \
               .1.3.6.1.4.1.9.9.42.1.2.2.1.20.""" + str(rttIndex) + """ s 'GET / HTTP/1.0\r\n' \
               .1.3.6.1.4.1.9.9.42.1.2.1.1.9.""" + str(rttIndex) + """ i 4
               """
        log.info("SLA Add cmd %s", cmd)

        os.system(str(cmd))
        return True

