from pysnmp.hlapi import *


with open('keys.txt') as fp: # file name with passwords. One password per line
    line = fp.readline()
    cnt = 1
    while line:
        print("Line {}: {}, {}".format(cnt, line.strip('\n'))))

        errorIndication, errorStatus, errorIndex, varBinds = next(
            getCmd(SnmpEngine(),
                   CommunityData(line.strip('\n'), line.strip('\n')),
                   # Replace stars with IP
                   UdpTransportTarget(('*.*.*.*', 161)), # IP and port of snmp agent
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
