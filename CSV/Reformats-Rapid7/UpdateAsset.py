import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def test(nAssets, data):
    print('sup')
    # print(nAssets)

def getIP(asset):
    try:
        return asset['Address']
    except:
        return ''

def getName(asset):
    try:
        return asset.name
    except:
        return ''

def getDesc(asset):
    try:
        return asset.loc['Description']
    except:
        try:
            return asset['Comments']
        except:
            return ''

def getSite(asset):
    try:
        return asset.loc['Site']
    except:
        try:
            return asset.loc['Application']
        except:
            return ''

def getOpSys(asset):
    try:
        return asset.loc['Operating System']
    except:
        return ''

def getEnv(asset):
    try:
        return asset.loc['Environment']
    except:
        return ''

def getPrevN(asset):
    try:
        return asset.loc['Previous Name']
    except:
        return ''

def getExploit(asset):
    try:
        return asset.loc['Exploits']
    except:
        return ''

def getMalware(asset):
    try:
        return asset.loc['Malware']
    except:
        return ''

def getVuln(asset):
    try:
        return asset.loc['Vulnerabilities']
    except:
        return ''

def getRisk(asset):
    try:
        return asset.loc['Risk']
    except:
        return ''

def getLastScan(asset):
    try:
        return asset.loc['Last Scan']
    except:
        return ''

def getAssessed(asset):
    try:
        return asset.loc['Assessed']
    except:
        return ''

#if a new asset is going to be created
def fillCellVals(asset):
    #print(asset)
    IP = getIP(asset)
    name = getName(asset)
    desc = getDesc(asset)
    site = getSite(asset)
    opSys = getOpSys(asset)
    env = getEnv(asset)
    prevN = getPrevN(asset)
    exploit = getExploit(asset)
    malware = getMalware(asset)
    vuln = getVuln(asset)
    risk = getRisk(asset)
    lastScan = getLastScan(asset)
    assessed = getAssessed(asset)

    return [{"Address":IP,
             "Name":name,
             "Description":desc,
             "Site":site,
             "Operating System":opSys,
             "Environment":env,
             "Previous Name":prevN,
             "Exploit":exploit,
             "Malware":malware,
             "Vulnerabilities":vuln,
             "Risk":risk,
             "Last Scan":lastScan,
             "Assessed":assessed}]
