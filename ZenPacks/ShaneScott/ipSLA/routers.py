from Products.ZenUtils.Ext import DirectRouter, DirectResponse
from Products import Zuul

class SLARouter(DirectRouter):
    def _getFacade(self):
        return Zuul.getFacade('sla', self.context)

    def manage_delSLAs(self, rttIndex, deviceIp, community):
        facade = self._getFacade()
        success, message = facade.manage_delSLAs(rttIndex, deviceIp, community)

        if success:
            return DirectResponse.succeed(jobId=message)
        else:
            return DirectResponse.fail(message)

    def manage_writeMemSLAs(self, deviceIp, community):
        facade = self._getFacade()
        success, message = facade.manage_writeMemSLAs(deviceIp, community)

        if success:
            return DirectResponse.succeed(jobId=message)
        else:
            return DirectResponse.fail(message)

    def manage_addTcpSLAs(self, newId, rttIndex, deviceIp, community, rttMonEchoAdminTargetAddress, rttMonEchoAdminTargetPort, rttMonScheduleAdminRttStartTime=1, rttMonCtrlAdminOwner="zenoss"):
        facade = self._getFacade()
        success, message = facade.manage_addTcpSLAs(newId, rttIndex, deviceIp, community, rttMonEchoAdminTargetAddress, rttMonEchoAdminTargetPort, rttMonScheduleAdminRttStartTime=1, rttMonCtrlAdminOwner="zenoss")

        if success:
            return DirectResponse.succeed(jobId=message)
        else:
            return DirectResponse.fail(message)

    def manage_addJitterSLAs(self, newId, rttIndex, deviceIp, community, rttMonEchoAdminTargetAddress, rttMonEchoAdminTargetPort, rttMonEchoAdminInterval=60, rttMonEchoAdminNumPackets=100, rttMonScheduleAdminRttStartTime=1, rttMonCtrlAdminOwner="zenoss"):
        facade = self._getFacade()
        success, message = facade.manage_addJitterSLAs(newId, rttIndex, deviceIp, community, rttMonEchoAdminTargetAddress, rttMonEchoAdminTargetPort, rttMonEchoAdminInterval=60, rttMonEchoAdminNumPackets=100, rttMonScheduleAdminRttStartTime=1, rttMonCtrlAdminOwner="zenoss")

        if success:
            return DirectResponse.succeed(jobId=message)
        else:
            return DirectResponse.fail(message)


    def manage_addDnsSLAs(self, newId, rttIndex, deviceIp, community, rttMonEchoAdminNameServer, rttMonEchoAdminTargetAddressString, rttMonScheduleAdminRttStartTime=1, rttMonCtrlAdminOwner="zenoss"):
        facade = self._getFacade()
        success, message = facade.manage_addDnsSLAs(newId, rttIndex, deviceIp, community, rttMonEchoAdminNameServer, rttMonEchoAdminTargetAddressString, rttMonScheduleAdminRttStartTime=1, rttMonCtrlAdminOwner="zenoss")

        if success:
            return DirectResponse.succeed(jobId=message)
        else:
            return DirectResponse.fail(message)


    def manage_addDhcpSLAs(self, newId, rttIndex, deviceIp, community, rttMonScheduleAdminRttStartTime=1, rttMonCtrlAdminOwner="zenoss"):
        facade = self._getFacade()
        success, message = facade.manage_addDhcpSLAs(newId, rttIndex, deviceIp, community, rttMonScheduleAdminRttStartTime=1, rttMonCtrlAdminOwner="zenoss")

        if success:
            return DirectResponse.succeed(jobId=message)
        else:
            return DirectResponse.fail(message)

    def manage_addEchoSLAs(self, newId, rttIndex, deviceIp, community, rttMonEchoAdminTargetAddress, rttMonScheduleAdminRttStartTime=1, rttMonCtrlAdminFrequency=60, rttMonCtrlAdminOwner="zenoss", rttMonCtrlAdminThreshold=5000, rttMonCtrlAdminTimeout=5):
        facade = self._getFacade()
        success, message = facade.manage_addEchoSLAs(newId, rttIndex, deviceIp, community, rttMonEchoAdminTargetAddress, rttMonScheduleAdminRttStartTime=1, rttMonCtrlAdminFrequency=60, rttMonCtrlAdminOwner="zenoss", rttMonCtrlAdminThreshold=5000, rttMonCtrlAdminTimeout=5)

        if success:
            return DirectResponse.succeed(jobId=message)
        else:
            return DirectResponse.fail(message)


    def manage_addHttpSLAs(self, newId, rttIndex, deviceIp, community, rttMonEchoAdminURL, rttMonScheduleAdminRttStartTime=1, rttMonCtrlAdminFrequency=60, rttMonCtrlAdminOwner="zenoss", rttMonCtrlAdminThreshold=5000, rttMonCtrlAdminTimeout=5):
        facade = self._getFacade()
        success, message = facade.manage_addHttpSLAs(newId, rttIndex, deviceIp, community, rttMonEchoAdminURL, rttMonScheduleAdminRttStartTime=1, rttMonCtrlAdminFrequency=60, rttMonCtrlAdminOwner="zenoss", rttMonCtrlAdminThreshold=5000, rttMonCtrlAdminTimeout=5)

        if success:
            return DirectResponse.succeed(jobId=message)
        else:
            return DirectResponse.fail(message)

