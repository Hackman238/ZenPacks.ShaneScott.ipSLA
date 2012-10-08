import copy
import logging
log = logging.getLogger('zen.ZenSLA')

import locale
from Globals import DTMLFile
from Globals import InitializeClass
from Products.ZenModel.OSComponent import OSComponent
from Products.ZenModel.ZenPackPersistence import ZenPackPersistence
from Products.ZenUtils.Utils import convToUnits, prepId
from Products.ZenRelations.RelSchema import ToManyCont, ToOne
from Products.ZenModel.ZenossSecurity import *
from AccessControl import ClassSecurityInfo

class SLAs(ZenPackPersistence, OSComponent): 
    # IP-SLA Object class

    ZENPACKID = 'ZenPacks.ShaneScott.ipSLA'

    portal_type = meta_type = 'SLAs'

    instance = ''
    rttMonCtrlAdminOwner = ''
    rttMonCtrlAdminTag = ''
    rttMonCtrlAdminRttType = ''
    rttMonCtrlAdminThreshold = ''
    rttMonCtrlAdminFrequency = ''
    rttMonCtrlAdminTimeout = ''
    rttMonCtrlAdminVerifyData = ''
    rttMonCtrlAdminStatus = ''
    rttMonCtrlAdminNvgen = ''
    rttMonCtrlAdminGroupName = ''
    rttMonEchoAdminProtocol = ''
    rttMonEchoAdminTargetAddress = ''
    rttMonEchoAdminPktDataRequestSize = ''
    rttMonEchoAdminPktDataResponseSize = ''
    rttMonEchoAdminTargetPort = ''
    rttMonEchoAdminSourceAddress = ''
    rttMonEchoAdminSourcePort = ''
    rttMonEchoAdminControlEnable = ''
    rttMonEchoAdminTOS = ''
    rttMonEchoAdminLSREnable = ''
    rttMonEchoAdminTargetAddressString = ''
    rttMonEchoAdminNameServer = ''
    rttMonEchoAdminOperation = ''
    rttMonEchoAdminHTTPVersion = ''
    rttMonEchoAdminURL = ''
    rttMonEchoAdminCache = ''
    rttMonEchoAdminInterval = ''
    rttMonEchoAdminNumPackets = ''
    rttMonEchoAdminProxy = ''
    rttMonEchoAdminString1 = ''
    rttMonEchoAdminString2 = ''
    rttMonEchoAdminString3 = ''
    rttMonEchoAdminString4 = ''
    rttMonEchoAdminString5 = ''
    rttMonEchoAdminMode = ''
    rttMonEchoAdminVrfName = ''
    rttMonEchoAdminCodecType = ''
    rttMonEchoAdminCodecInterval = ''
    rttMonEchoAdminCodecPayload = ''
    rttMonEchoAdminCodecNumPackets = ''
    rttMonEchoAdminICPIFAdvFactor = ''
    rttMonEchoAdminLSPFECType = ''
    rttMonEchoAdminLSPSelector = ''
    rttMonEchoAdminLSPReplyMode = ''
    rttMonEchoAdminLSPTTL = ''
    rttMonEchoAdminLSPExp = ''
    rttMonEchoAdminPrecision = ''
    rttMonEchoAdminProbePakPriority = ''
    rttMonEchoAdminOWNTPSyncTolAbs = ''
    rttMonEchoAdminOWNTPSyncTolPct = ''
    rttMonEchoAdminOWNTPSyncTolType = ''
    rttMonEchoAdminCalledNumber = ''
    rttMonEchoAdminDetectPoint = ''
    rttMonEchoAdminGKRegistration = ''
    rttMonEchoAdminSourceVoicePort = ''
    rttMonEchoAdminCallDuration = ''
    rttMonEchoAdminLSPReplyDscp = ''
    rttMonEchoAdminLSPNullShim = ''
    rttMonEchoAdminTargetMPID = ''
    rttMonEchoAdminTargetDomainName = ''
    rttMonEchoAdminTargetVLAN = ''
    rttMonEchoAdminEthernetCOS = ''
    rttMonEchoAdminLSPVccvID = ''
    rttMonEchoAdminTargetEVC = ''

    _properties = OSComponent._properties + (
        {'id':'instance', 'type':'string', 'mode':'w'},
        {'id':'rttMonCtrlAdminOwner', 'type':'string', 'mode':'w'},
        {'id':'rttMonCtrlAdminTag', 'type':'string', 'mode':'w'},
        {'id':'rttMonCtrlAdminRttType', 'type':'string', 'mode':'w'},
        {'id':'rttMonCtrlAdminThreshold', 'type':'int', 'mode':'w'},
        {'id':'rttMonCtrlAdminFrequency', 'type':'int', 'mode':'w'},
        {'id':'rttMonCtrlAdminTimeout', 'type':'int', 'mode':'w'},
        {'id':'rttMonCtrlAdminVerifyData', 'type':'int', 'mode':'w'},
        {'id':'rttMonCtrlAdminStatus', 'type':'int', 'mode':'w'},
        {'id':'rttMonCtrlAdminNvgen', 'type':'float', 'mode':'w'},
        {'id':'rttMonCtrlAdminGroupName', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminProtocol', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminTargetAddress', 'type':'int', 'mode':'w'},
        {'id':'rttMonEchoAdminPktDataRequestSize', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminPktDataResponseSize', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminTargetPort', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminSourceAddress', 'type':'int', 'mode':'w'},
        {'id':'rttMonEchoAdminSourcePort', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminControlEnable', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminTOS', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminLSREnable', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminTargetAddressString', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminNameServer', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminOperation', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminHTTPVersion', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminURL', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminCache', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminInterval', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminNumPackets', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminProxy', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminString1', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminString2', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminString3', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminString4', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminString5', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminMode', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminVrfName', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminCodecType', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminCodecInterval', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminCodecPayload', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminCodecNumPackets', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminICPIFAdvFactor', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminLSPFECType', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminLSPSelector', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminLSPReplyMode', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminLSPTTL', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminLSPExp', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminPrecision', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminProbePakPriority', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminOWNTPSyncTolAbs', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminOWNTPSyncTolPct', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminOWNTPSyncTolType', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminCalledNumber', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminDetectPoint', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminGKRegistration', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminSourceVoicePort', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminCallDuration', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminLSPReplyDscp', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminLSPNullShim', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminTargetMPID', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminTargetDomainName', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminTargetVLAN', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminEthernetCOS', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminLSPVccvID', 'type':'string', 'mode':'w'},
        {'id':'rttMonEchoAdminTargetEVC', 'type':'string', 'mode':'w'},
        )

    _relations = OSComponent._relations + (('os', ToOne(ToManyCont, 'Products.ZenModel.OperatingSystem', 'ipSLAs')),)

    slaTypeMap = ('ECHO', 'HTTP', 'DNS', 'DHCP')

    factory_type_information = (
        {
            'id'         : 'SLAs',
            'meta_type'      : 'SLAs',
            'description'    : '''IP Service Level Agreement Test Object''',
            'icon'       : 'Device_icon.gif',
            'product'    : 'SLAs',
            'factory'    : 'manage_addSLAs',
            'immediate_view' : 'ipSLAsPerformance',
            'actions'    :
            (
                { 'id'        : 'templates'
                , 'name'      : 'Templates'
                , 'action'    : 'objTemplates'
                , 'permissions'   : (ZEN_CHANGE_SETTINGS, )
                },
            )
        },
    )


    security = ClassSecurityInfo()

    def __init__(self, id, title = None):
        # Init OSComponent
        OSComponent.__init__(self, id, title)


    def deviceId(self):
        # The device id, for indexing purposes.
        d = self.device()
        if d:
           return d.getPrimaryId()
        else:
           return None

    def getId(self):
        return self.id

    def getRttMonCtrlAdminRttType(self):
        return self.rttMonCtrlAdminRttType

    def getRttMonCtrlAdminOwner(self):
        return self.rttMonCtrlAdminOwner

    def getRttMonCtrlAdminTag(self):
        return self.rttMonCtrlAdminTag

    def viewName(self):
        return self.rttMonCtrlAdminTag
    name = primarySortKey = viewName


    def managedDeviceLink(self):
        from Products.ZenModel.ZenModelRM import ZenModelRM
        d = self.getDmdRoot('Devices').findDevice(self.rttMonCtrlAdminTag)
        if d:
            return ZenModelRM.urlLink(d, 'link')
        return None

    def manage_editProperties(self, REQUEST):
        # Override from propertiyManager so we can trap errors
        try:
            return ConfmonPropManager.manage_editProperties(self, REQUEST)
        except IpAddressError, e:
            return   MessageDialog(
             title = 'Input Error',
             message = e.args[0],
             action = 'manage_main')

    def getRRDTemplateName(self):
        # Return the interface type as the target type name.
        return self.prepId(self.rttMonCtrlAdminRttType or 'Unknown')

    def getRRDTemplates(self):
        # Return a list containing the appropriate RRDTemplate for this SLA.
        templateName = self.getRRDTemplateName()
        default = self.getRRDTemplateByName(templateName)

        if not default:
            default = self.getRRDTemplateByName('New_SLA')

        if default:
            return [default]
        return []

InitializeClass(SLAs)
