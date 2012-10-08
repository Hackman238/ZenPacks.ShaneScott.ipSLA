from Products.Zuul.interfaces import IInfo, IComponentInfo
from Products.Zuul.form import schema
from Products.Zuul.utils import ZuulMessageFactory as _t

from Products.Zuul.interfaces import IFacade
from Products.Zuul.interfaces import IDeviceInfo

from Products.ZenModel.ZVersion import VERSION as ZENOSS_VERSION
from Products.ZenUtils.Version import Version

if Version.parse('Zenoss %s' % ZENOSS_VERSION) >= Version.parse('Zenoss 4'):
    SingleLineText = schema.TextLine
    MultiLineText = schema.Text
else:
    SingleLineText = schema.Text
    MultiLineText = schema.TextLine

class ISLAFacade(IFacade):
    def manage_delSLAs(self, rttIndex, deviceIp, community):
        '''Delete a SLA on a host'''


    def manage_writeMemSLAs(self, deviceIp, community):
        '''Write mem on a host'''


    def manage_addTcpSLAs(self, newId, rttIndex, deviceIp, community, rttMonEchoAdminTargetAddress, rttMonEchoAdminTargetPort, rttMonScheduleAdminRttStartTime=1, rttMonCtrlAdminOwner='zenoss'):
        '''Add a SLA to this SLA host'''


    def manage_addJitterSLAs(self, newId, rttIndex, deviceIp, community, rttMonEchoAdminTargetAddress, rttMonEchoAdminTargetPort, rttMonEchoAdminInterval=60, rttMonEchoAdminNumPackets=100, rttMonScheduleAdminRttStartTime=1, rttMonCtrlAdminOwner='zenoss'):
        '''Add a SLA to this SLA host'''


    def manage_addDnsSLAs(self, newId, rttIndex, deviceIp, community, rttMonEchoAdminNameServer, rttMonEchoAdminTargetAddressString, rttMonScheduleAdminRttStartTime=1, rttMonCtrlAdminOwner='zenoss'):
        '''Add a SLA to this SLA host'''


    def manage_addDhcpSLAs(self, newId, rttIndex, deviceIp, community, rttMonScheduleAdminRttStartTime=1, rttMonCtrlAdminOwner='zenoss'):
        '''Add a SLA to this SLA host'''


    def manage_addEchoSLAs(self, newId, rttIndex, deviceIp, community, rttMonEchoAdminTargetAddress, rttMonScheduleAdminRttStartTime=1, rttMonCtrlAdminFrequency=60, rttMonCtrlAdminOwner='zenoss', rttMonCtrlAdminThreshold=5000, rttMonCtrlAdminTimeout=5):
        '''Add a SLA to this SLA host'''


    def manage_addHttpSLAs(self, newId, rttIndex, deviceIp, community, rttMonEchoAdminURL, rttMonScheduleAdminRttStartTime=1, rttMonCtrlAdminFrequency=60, rttMonCtrlAdminOwner='zenoss', rttMonCtrlAdminThreshold=5000, rttMonCtrlAdminTimeout=5):
        '''Add a SLA to this SLA host'''


class ISLADataSourceInfo(IInfo):
    newId = schema.Text(title=_t(u'Name'),
                       xtype='idfield',
                       description=_t(u'The name of this datasource'))
    type = schema.Text(title=_t(u'Type'),
                       readonly=True)
    oid = schema.Text(title=_t(u'OID'))
    enabled = schema.Bool(title=_t(u'Enabled'))

class ISLAsInfo(IComponentInfo):
    '''
    Info adapter for SLAs components.
    '''
    instance = schema.Text(title=_t(u'Instance'), readonly=True, group='Overview')
    rttMonCtrlAdminOwner = schema.Text(title=_t(u'Owner'), readonly=True, group='Details')
    rttMonCtrlAdminTag = schema.Text(title=_t(u'Tag'), readonly=True, group='Details')
    rttMonCtrlAdminRttType = schema.Text(title=_t(u'Type'), readonly=True, group='Overview')
    rttMonCtrlAdminThreshold = schema.Text(title=_t(u'Threshold'), readonly=True, group='Details')
    rttMonCtrlAdminFrequency = schema.Text(title=_t(u'Frequency'), readonly=True, group='Overview')
    rttMonCtrlAdminTimeout = schema.Text(title=_t(u'Timeout'), readonly=True, group='Details')
    rttMonCtrlAdminVerifyData = schema.Text(title=_t(u'Verify'), readonly=True, group='Details')
    rttMonCtrlAdminStatus = schema.Text(title=_t(u'Status'), readonly=True, group='Overview')
    rttMonCtrlAdminNvgen = schema.Text(title=_t(u'NVGen'), readonly=True, group='Details')
    rttMonCtrlAdminGroupName = schema.Text(title=_t(u'Group'), readonly=True, group='Overview')
    rttMonEchoAdminProtocol = schema.Text(title=_t(u'Type'), readonly=True, group='Details')
    rttMonEchoAdminTargetAddress = schema.Text(title=_t(u'Echo Target'), readonly=True, group='Details')
    rttMonEchoAdminPktDataRequestSize = schema.Text(title=_t(u'Request packet size'), readonly=True, group='Details')
    rttMonEchoAdminPktDataResponseSize = schema.Text(title=_t(u'Repsonse packet size'), readonly=True, group='Details')
    rttMonEchoAdminTargetPort = schema.Text(title=_t(u'Target port'), readonly=True, group='Details')
    rttMonEchoAdminSourceAddress = schema.Text(title=_t(u'Source'), readonly=True, group='Details')
    rttMonEchoAdminSourcePort = schema.Text(title=_t(u'Source port'), readonly=True, group='Details')
    rttMonEchoAdminControlEnable = schema.Text(title=_t(u'Enabled'), readonly=True, group='Details')
    rttMonEchoAdminTOS = schema.Text(title=_t(u'TOS'), readonly=True, group='Details')
    rttMonEchoAdminLSREnable = schema.Text(title=_t(u'LSR'), readonly=True, group='Details')
    rttMonEchoAdminTargetAddressString = schema.Text(title=_t(u'Target String'), readonly=True, group='Details')
    rttMonEchoAdminNameServer = schema.Text(title=_t(u'Name server'), readonly=True, group='Details')
    rttMonEchoAdminOperation = schema.Text(title=_t(u'Operation'), readonly=True, group='Details')
    rttMonEchoAdminHTTPVersion = schema.Text(title=_t(u'HTTP Version'), readonly=True, group='Details')
    rttMonEchoAdminURL = schema.Text(title=_t(u'URL'), readonly=True, group='Details')
    rttMonEchoAdminCache = schema.Text(title=_t(u'Cached'), readonly=True, group='Details')
    rttMonEchoAdminInterval = schema.Text(title=_t(u'Interval'), readonly=True, group='Details')
    rttMonEchoAdminNumPackets = schema.Text(title=_t(u'Packet count'), readonly=True, group='Details')
    rttMonEchoAdminProxy = schema.Text(title=_t(u'Proxy'), readonly=True, group='Details')
    rttMonEchoAdminString1 = schema.Text(title=_t(u'String 1'), readonly=True, group='Details')
    rttMonEchoAdminString2 = schema.Text(title=_t(u'String 2'), readonly=True, group='Details')
    rttMonEchoAdminString3 = schema.Text(title=_t(u'String 3'), readonly=True, group='Details')
    rttMonEchoAdminString4 = schema.Text(title=_t(u'String 4'), readonly=True, group='Details')
    rttMonEchoAdminString5 = schema.Text(title=_t(u'String 5'), readonly=True, group='Details')
    rttMonEchoAdminMode = schema.Text(title=_t(u'Mode'), readonly=True, group='Details')
    rttMonEchoAdminVrfName = schema.Text(title=_t(u'VRF Name'), readonly=True, group='Details')
    rttMonEchoAdminCodecType = schema.Text(title=_t(u'Codec'), readonly=True, group='Details')
    rttMonEchoAdminCodecInterval = schema.Text(title=_t(u'Codec interval'), readonly=True, group='Details')
    rttMonEchoAdminCodecPayload = schema.Text(title=_t(u'Codec payload'), readonly=True, group='Details')
    rttMonEchoAdminCodecNumPackets = schema.Text(title=_t(u'Codec packet count'), readonly=True, group='Details')
    rttMonEchoAdminICPIFAdvFactor = schema.Text(title=_t(u'ICPIF Adv factor'), readonly=True, group='Details')
    rttMonEchoAdminLSPFECType = schema.Text(title=_t(u'LSP FEC type'), readonly=True, group='Details')
    rttMonEchoAdminLSPSelector = schema.Text(title=_t(u'LSP selector'), readonly=True, group='Details')
    rttMonEchoAdminLSPReplyMode = schema.Text(title=_t(u'LSP reply mode'), readonly=True, group='Details')
    rttMonEchoAdminLSPTTL = schema.Text(title=_t(u'LSP TTL'), readonly=True, group='Details')
    rttMonEchoAdminLSPExp = schema.Text(title=_t(u'LSP Exp'), readonly=True, group='Details')
    rttMonEchoAdminPrecision = schema.Text(title=_t(u'Precision'), readonly=True, group='Details')
    rttMonEchoAdminProbePakPriority = schema.Text(title=_t(u'Probe priority'), readonly=True, group='Details')
    rttMonEchoAdminOWNTPSyncTolAbs = schema.Text(title=_t(u'OWNTP sync tol Abs'), readonly=True, group='Details')
    rttMonEchoAdminOWNTPSyncTolPct = schema.Text(title=_t(u'OWNTP sync tol Pct'), readonly=True, group='Details')
    rttMonEchoAdminOWNTPSyncTolType = schema.Text(title=_t(u'OWNTP sync tol type'), readonly=True, group='Details')
    rttMonEchoAdminCalledNumber = schema.Text(title=_t(u'Called number'), readonly=True, group='Details')
    rttMonEchoAdminDetectPoint = schema.Text(title=_t(u'Detection point'), readonly=True, group='Details')
    rttMonEchoAdminGKRegistration = schema.Text(title=_t(u'GK registration'), readonly=True, group='Details')
    rttMonEchoAdminSourceVoicePort = schema.Text(title=_t(u'Source voice port'), readonly=True, group='Details')
    rttMonEchoAdminCallDuration = schema.Text(title=_t(u'Call duration'), readonly=True, group='Details')
    rttMonEchoAdminLSPReplyDscp = schema.Text(title=_t(u'LSP reply Description'), readonly=True, group='Details')
    rttMonEchoAdminLSPNullShim = schema.Text(title=_t(u'LSP Shim'), readonly=True, group='Details')
    rttMonEchoAdminTargetMPID = schema.Text(title=_t(u'Target MPID'), readonly=True, group='Details')
    rttMonEchoAdminTargetDomainName = schema.Text(title=_t(u'Target domain'), readonly=True, group='Details')
    rttMonEchoAdminTargetVLAN = schema.Text(title=_t(u'Target VLAN'), readonly=True, group='Details')
    rttMonEchoAdminEthernetCOS = schema.Text(title=_t(u'Ethernet COS'), readonly=True, group='Details')
    rttMonEchoAdminLSPVccvID = schema.Text(title=_t(u'LSP Vccv ID'), readonly=True, group='Details')
    rttMonEchoAdminTargetEVC = schema.Text(title=_t(u'Target EVC'), readonly=True, group='Details')
