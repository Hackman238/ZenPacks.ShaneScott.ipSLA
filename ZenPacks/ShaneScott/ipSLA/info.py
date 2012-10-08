from zope.component import adapts
from zope.interface import implements

from Products.ZenUtils.Utils import convToUnits

from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.component import ComponentInfo
from Products.Zuul.infos.template import RRDDataSourceInfo

from ZenPacks.ShaneScott.ipSLA.SLAs import SLAs
from ZenPacks.ShaneScott.ipSLA.interfaces import ISLADataSourceInfo, ISLAsInfo

class SLAsInfo(ComponentInfo):
    implements(ISLAsInfo)
    adapts(SLAs)

    instance = ProxyProperty('instance')
    rttMonCtrlAdminRttType = ProxyProperty('rttMonCtrlAdminRttType')
    rttMonCtrlAdminOwner = ProxyProperty('rttMonCtrlAdminOwner')
    rttMonCtrlAdminTag = ProxyProperty('rttMonCtrlAdminTag')
    rttMonCtrlAdminRttType = ProxyProperty('rttMonCtrlAdminRttType')
    rttMonCtrlAdminThreshold = ProxyProperty('rttMonCtrlAdminThreshold')
    rttMonCtrlAdminFrequency = ProxyProperty('rttMonCtrlAdminFrequency')
    rttMonCtrlAdminTimeout = ProxyProperty('rttMonCtrlAdminTimeout')
    rttMonCtrlAdminVerifyData = ProxyProperty('rttMonCtrlAdminVerifyData')
    rttMonCtrlAdminStatus = ProxyProperty('rttMonCtrlAdminStatus')
    rttMonCtrlAdminNvgen = ProxyProperty('rttMonCtrlAdminNvgen')
    rttMonCtrlAdminGroupName = ProxyProperty('rttMonCtrlAdminGroupName')
    rttMonEchoAdminProtocol = ProxyProperty('rttMonEchoAdminProtocol')
    rttMonEchoAdminTargetAddress = ProxyProperty('rttMonEchoAdminTargetAddress')
    rttMonEchoAdminPktDataRequestSize = ProxyProperty('rttMonEchoAdminPktDataRequestSize')
    rttMonEchoAdminPktDataResponseSize = ProxyProperty('rttMonEchoAdminPktDataResponseSize')
    rttMonEchoAdminTargetPort = ProxyProperty('rttMonEchoAdminTargetPort')
    rttMonEchoAdminSourceAddress = ProxyProperty('rttMonEchoAdminSourceAddress')
    rttMonEchoAdminSourcePort = ProxyProperty('rttMonEchoAdminSourcePort')
    rttMonEchoAdminControlEnable = ProxyProperty('rttMonEchoAdminControlEnable')
    rttMonEchoAdminTOS = ProxyProperty('rttMonEchoAdminTOS')
    rttMonEchoAdminLSREnable = ProxyProperty('rttMonEchoAdminLSREnable')
    rttMonEchoAdminTargetAddressString = ProxyProperty('rttMonEchoAdminTargetAddressString')
    rttMonEchoAdminNameServer = ProxyProperty('rttMonEchoAdminNameServer')
    rttMonEchoAdminOperation = ProxyProperty('rttMonEchoAdminOperation')
    rttMonEchoAdminHTTPVersion = ProxyProperty('rttMonEchoAdminHTTPVersion')
    rttMonEchoAdminURL = ProxyProperty('rttMonEchoAdminURL')
    rttMonEchoAdminCache = ProxyProperty('rttMonEchoAdminCache')
    rttMonEchoAdminInterval = ProxyProperty('rttMonEchoAdminInterval')
    rttMonEchoAdminNumPackets = ProxyProperty('rttMonEchoAdminNumPackets')
    rttMonEchoAdminProxy = ProxyProperty('rttMonEchoAdminProxy')
    rttMonEchoAdminString1 = ProxyProperty('rttMonEchoAdminString1')
    rttMonEchoAdminString2 = ProxyProperty('rttMonEchoAdminString2')
    rttMonEchoAdminString3 = ProxyProperty('rttMonEchoAdminString3')
    rttMonEchoAdminString4 = ProxyProperty('rttMonEchoAdminString4')
    rttMonEchoAdminString5 = ProxyProperty('rttMonEchoAdminString5')
    rttMonEchoAdminMode = ProxyProperty('rttMonEchoAdminMode')
    rttMonEchoAdminVrfName = ProxyProperty('rttMonEchoAdminVrfName')
    rttMonEchoAdminCodecType = ProxyProperty('rttMonEchoAdminCodecType')
    rttMonEchoAdminCodecInterval = ProxyProperty('rttMonEchoAdminCodecInterval')
    rttMonEchoAdminCodecPayload = ProxyProperty('rttMonEchoAdminCodecPayload')
    rttMonEchoAdminCodecNumPackets = ProxyProperty('rttMonEchoAdminCodecNumPackets')
    rttMonEchoAdminICPIFAdvFactor = ProxyProperty('rttMonEchoAdminICPIFAdvFactor')
    rttMonEchoAdminLSPFECType = ProxyProperty('rttMonEchoAdminLSPFECType')
    rttMonEchoAdminLSPSelector = ProxyProperty('rttMonEchoAdminLSPSelector')
    rttMonEchoAdminLSPReplyMode = ProxyProperty('rttMonEchoAdminLSPReplyMode')
    rttMonEchoAdminLSPTTL = ProxyProperty('rttMonEchoAdminLSPTTL')
    rttMonEchoAdminLSPExp = ProxyProperty('rttMonEchoAdminLSPExp')
    rttMonEchoAdminPrecision = ProxyProperty('rttMonEchoAdminPrecision')
    rttMonEchoAdminProbePakPriority = ProxyProperty('rttMonEchoAdminProbePakPriority')
    rttMonEchoAdminOWNTPSyncTolAbs = ProxyProperty('rttMonEchoAdminOWNTPSyncTolAbs')
    rttMonEchoAdminOWNTPSyncTolPct = ProxyProperty('rttMonEchoAdminOWNTPSyncTolPct')
    rttMonEchoAdminOWNTPSyncTolType = ProxyProperty('rttMonEchoAdminOWNTPSyncTolType')
    rttMonEchoAdminCalledNumber = ProxyProperty('rttMonEchoAdminCalledNumber')
    rttMonEchoAdminDetectPoint = ProxyProperty('rttMonEchoAdminDetectPoint')
    rttMonEchoAdminGKRegistration = ProxyProperty('rttMonEchoAdminGKRegistration')
    rttMonEchoAdminSourceVoicePort = ProxyProperty('rttMonEchoAdminSourceVoicePort')
    rttMonEchoAdminCallDuration = ProxyProperty('rttMonEchoAdminCallDuration')
    rttMonEchoAdminLSPReplyDscp = ProxyProperty('rttMonEchoAdminLSPReplyDscp')
    rttMonEchoAdminLSPNullShim = ProxyProperty('rttMonEchoAdminLSPNullShim')
    rttMonEchoAdminTargetMPID = ProxyProperty('rttMonEchoAdminTargetMPID')
    rttMonEchoAdminTargetDomainName = ProxyProperty('rttMonEchoAdminTargetDomainName')
    rttMonEchoAdminTargetVLAN = ProxyProperty('rttMonEchoAdminTargetVLAN')
    rttMonEchoAdminEthernetCOS = ProxyProperty('rttMonEchoAdminEthernetCOS')
    rttMonEchoAdminLSPVccvID = ProxyProperty('rttMonEchoAdminLSPVccvID')
    rttMonEchoAdminTargetEVC = ProxyProperty('rttMonEchoAdminTargetEVC')

    @property
    def rttMonCtrlAdminRttType(self):
        return self._object.getRttMonCtrlAdminRttType()

    @property
    def rttMonCtrlAdminOwner(self):
        return self._object.getRttMonCtrlAdminOwner()

    @property
    def rttMonCtrlAdminTag(self):
        return self._object.getRttMonCtrlAdminTag()


class SLADataSourceInfo(RRDDataSourceInfo):
    implements(ISLADataSourceInfo)

    def __init__(self, dataSource):
        self._object = dataSource

    @property
    def testable(self):
        return False

    @property
    def id(self):
        return '/'.join(self._object.getPrimaryPath())

    @property
    def source(self):
        return self._object.getDescription()

    @property
    def type(self):
        return self._object.sourcetype

    enabled = ProxyProperty('enabled')

    @property
    def availableParsers(self):
        '''
        returns a list of all available parsers
        '''
        if hasattr(self._object, 'parsers'):
            return self._object.parsers()
        return []

    # severity
    def _setSeverity(self, value):
        try:
            if isinstance(value, str):
                value = severityId(value)
        except ValueError:
            # they entered junk somehow (default to info if invalid)
            value = severityId('info')
        self._object.severity = value

    def _getSeverity(self):
        return self._object.getSeverityString()

    @property
    def newId(self):
        return self._object.id

    severity = property(_getSeverity, _setSeverity)
    cycletime = ProxyProperty('cycletime')
    eventClass = ProxyProperty('eventClass')
    oid = ProxyProperty('oid')
