import Globals
from Products.ZenModel.ZenPackPersistence import ZenPackPersistence
from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap, MultiArgs
from struct import *
import sys
import string

class SLA(ZenPackPersistence, SnmpPlugin):

        ZENPACKID = 'ZenPacks.ShaneScott.ipSLA'

        maptype = "ipSLAMap"
        compname = "os"
        relname = "ipSLAs"
        modname = 'ZenPacks.ShaneScott.ipSLA.SLAs'

        cMonOperEntry = {
                '.1.1.2': 'rttMonCtrlAdminOwner',
                '.1.1.3': 'rttMonCtrlAdminTag',
                '.1.1.4': 'rttMonCtrlAdminRttType',
                '.1.1.5': 'rttMonCtrlAdminThreshold',
                '.1.1.6': 'rttMonCtrlAdminFrequency',
                '.1.1.7': 'rttMonCtrlAdminTimeout',
                '.1.1.8': 'rttMonCtrlAdminVerifyData',
                '.1.1.9': 'rttMonCtrlAdminStatus',
                '.1.1.10': 'rttMonCtrlAdminNvgen',
                '.1.1.11': 'rttMonCtrlAdminGroupName',
                '.2.1.1': 'rttMonEchoAdminProtocol',
                '.2.1.2': 'rttMonEchoAdminTargetAddress',
                '.2.1.3': 'rttMonEchoAdminPktDataRequestSize',
                '.2.1.4': 'rttMonEchoAdminPktDataResponseSize',
                '.2.1.5': 'rttMonEchoAdminTargetPort',
                '.2.1.6': 'rttMonEchoAdminSourceAddress',
                '.2.1.7': 'rttMonEchoAdminSourcePort',
                '.2.1.8': 'rttMonEchoAdminControlEnable',
                '.2.1.9': 'rttMonEchoAdminTOS',
                '.2.1.10': 'rttMonEchoAdminLSREnable',
                '.2.1.11': 'rttMonEchoAdminTargetAddressString',
                '.2.1.12': 'rttMonEchoAdminNameServer',
                '.2.1.13': 'rttMonEchoAdminOperation',
                '.2.1.14': 'rttMonEchoAdminHTTPVersion',
                '.2.1.15': 'rttMonEchoAdminURL',
                '.2.1.16': 'rttMonEchoAdminCache',
                '.2.1.17': 'rttMonEchoAdminInterval',
                '.2.1.18': 'rttMonEchoAdminNumPackets',
                '.2.1.19': 'rttMonEchoAdminProxy',
                '.2.1.20': 'rttMonEchoAdminString1',
                '.2.1.21': 'rttMonEchoAdminString2',
                '.2.1.22': 'rttMonEchoAdminString3',
                '.2.1.23': 'rttMonEchoAdminString4',
                '.2.1.24': 'rttMonEchoAdminString5',
                '.2.1.25': 'rttMonEchoAdminMode',
                '.2.1.26': 'rttMonEchoAdminVrfName',
                '.2.1.27': 'rttMonEchoAdminCodecType',
                '.2.1.28': 'rttMonEchoAdminCodecInterval',
                '.2.1.29': 'rttMonEchoAdminCodecPayload',
                '.2.1.30': 'rttMonEchoAdminCodecNumPackets',
                '.2.1.31': 'rttMonEchoAdminICPIFAdvFactor',
                '.2.1.32': 'rttMonEchoAdminLSPFECType',
                '.2.1.33': 'rttMonEchoAdminLSPSelector',
                '.2.1.34': 'rttMonEchoAdminLSPReplyMode',
                '.2.1.35': 'rttMonEchoAdminLSPTTL',
                '.2.1.36': 'rttMonEchoAdminLSPExp',
                '.2.1.37': 'rttMonEchoAdminPrecision',
                '.2.1.38': 'rttMonEchoAdminProbePakPriority',
                '.2.1.39': 'rttMonEchoAdminOWNTPSyncTolAbs',
                '.2.1.40': 'rttMonEchoAdminOWNTPSyncTolPct',
                '.2.1.41': 'rttMonEchoAdminOWNTPSyncTolType',
                '.2.1.42': 'rttMonEchoAdminCalledNumber',
                '.2.1.43': 'rttMonEchoAdminDetectPoint',
                '.2.1.44': 'rttMonEchoAdminGKRegistration',
                '.2.1.45': 'rttMonEchoAdminSourceVoicePort',
                '.2.1.46': 'rttMonEchoAdminCallDuration',
                '.2.1.47': 'rttMonEchoAdminLSPReplyDscp',
                '.2.1.48': 'rttMonEchoAdminLSPNullShim',
                '.2.1.49': 'rttMonEchoAdminTargetMPID',
                '.2.1.50': 'rttMonEchoAdminTargetDominName',
                '.2.1.51': 'rttMonEchoAdminTargetVLAN',
                '.2.1.52': 'rttMonEchoAdminEthernetCOS',
                '.2.1.53': 'rttMonEchoAdminLSPVccvID',
                '.2.1.54': 'rttMonEchoAdminTargetEVC',
        }

        snmpGetTableMaps = (
                GetTableMap('MonOperEntry', '.1.3.6.1.4.1.9.9.42.1.2', cMonOperEntry),
        )


        def process(self, device, results, log):
                """
                collect SLA information from ost device
                """

                log.info('processing %s for device %s', self.name(), device.id)
                log.info("SLA (entries) results: %r", results)
                getdata, tabledata = results
                table = tabledata.get("MonOperEntry")
                rm = self.relMap()
                count=-1 

		for info in table.values():
			keys = table.keys()
			count=count+1
			log.info('info: %s', info)
			om = self.objectMap(info)
                        om.id = (self.prepId(om.rttMonCtrlAdminTag) or self.prepId('SLA_' + str(om.rttMonCtrlAdminRttType)))
                        om.instance = keys[count]

                        if om.rttMonCtrlAdminRttType == 1:
                                om.rttMonCtrlAdminRttType = "Echo"

                        if om.rttMonCtrlAdminRttType == 2:
                                om.rttMonCtrlAdminRttType = "PathEcho"

                        if om.rttMonCtrlAdminRttType == 3:

                                om.rttMonCtrlAdminRttType = "FileIO"

                        if om.rttMonCtrlAdminRttType == 4:
                                om.rttMonCtrlAdminRttType = "Script"

                        if om.rttMonCtrlAdminRttType == 5:
                                om.rttMonCtrlAdminRttType = "UDPEcho"

                        if om.rttMonCtrlAdminRttType == 6:
                                om.rttMonCtrlAdminRttType = "TCPConnect"

                        if om.rttMonCtrlAdminRttType == 7:
                                om.rttMonCtrlAdminRttType = "HTTP"

                        if om.rttMonCtrlAdminRttType == 8:

                                om.rttMonCtrlAdminRttType = "DNS"

                        if om.rttMonCtrlAdminRttType == 9:
                                om.rttMonCtrlAdminRttType = "Jitter"        

                        if om.rttMonCtrlAdminRttType == 11:
                                om.rttMonCtrlAdminRttType = "DHCP"

                        if om.rttMonCtrlAdminRttType == 12:
                                om.rttMonCtrlAdminRttType = "FTP"

                        if om.rttMonCtrlAdminRttType == 13:
                                om.rttMonCtrlAdminRttType = "VoIP"

                        if om.rttMonCtrlAdminRttType == 14:

                                om.rttMonCtrlAdminRttType = "RTP"

                        if om.rttMonCtrlAdminRttType == 15:
                                om.rttMonCtrlAdminRttType = "LSPGroup"

                        if om.rttMonCtrlAdminRttType == 16:
                                om.rttMonCtrlAdminRttType = "ICMPJitter"

                        if om.rttMonCtrlAdminRttType == 17:
                                om.rttMonCtrlAdminRttType = "LSPPing"

                        if om.rttMonCtrlAdminRttType == 18:
                                om.rttMonCtrlAdminRttType = "LSPTrace"

		        log.debug('om.instance %s', om.instance)

			try:
				FrttMonEchoAdminNameServer = str(unpack('!4B',om.rttMonEchoAdminNameServer))
                                FrttMonEchoAdminNameServer = FrttMonEchoAdminNameServer.replace(",", ".")
                                FrttMonEchoAdminNameServer = FrttMonEchoAdminNameServer.replace("(", "")
                                FrttMonEchoAdminNameServer = FrttMonEchoAdminNameServer.replace(")", "")
                                om.rttMonEchoAdminNameServer = FrttMonEchoAdminNameServer
                        except:
                                log.info("DEBUGGER NS unpack hiccup.")

                        try:
                                FrttMonEchoAdminSourceAddress = str(unpack('!4B',om.rttMonEchoAdminSourceAddress))
                                FrttMonEchoAdminSourceAddress = FrttMonEchoAdminSourceAddress.replace(",", ".")
                                FrttMonEchoAdminSourceAddress = FrttMonEchoAdminSourceAddress.replace("(", "")
                                FrttMonEchoAdminSourceAddress = FrttMonEchoAdminSourceAddress.replace(")", "")
                                om.rttMonEchoAdminSourceAddress = FrttMonEchoAdminSourceAddress
                        except:
                                log.info("DEBUGGER Source unpack hiccup.")
			
			try:	
				FrttMonEchoAdminTargetAddress = str(unpack('!4B',om.rttMonEchoAdminTargetAddress))
				FrttMonEchoAdminTargetAddress = FrttMonEchoAdminTargetAddress.replace(",", ".")
				FrttMonEchoAdminTargetAddress = FrttMonEchoAdminTargetAddress.replace("(", "")
				FrttMonEchoAdminTargetAddress = FrttMonEchoAdminTargetAddress.replace(")", "")
				om.rttMonEchoAdminTargetAddress = FrttMonEchoAdminTargetAddress
			except:
				log.info("DEBUGGER Target unpack hiccup.")
			
			rm.append(om)


                log.debug("rm: %s", rm)
		return [rm]
