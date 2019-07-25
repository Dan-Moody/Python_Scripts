from pysnmp.hlapi import *


errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
    # Replace stars with IP
    UdpTransportTarget(('*.*.*.*', 161)), # IP and port of SNMP agent
    ContextData(),
    ObjectType(ObjectIdentity('1.3.6.1.2.1.1.1.0'))) # OID for MIB data
)




if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
else:
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))
