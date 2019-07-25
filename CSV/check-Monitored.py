import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Reads in a csv of IPs that have been scanned and compared it with a master list
# in an attempt to find which IPs we are not properly monitoring
#
# The next section contains the file names that should be changed depending on what
# your csv files are named

#--------------------------------------------------------------------

# CSV name you want to compare with master list
# Change this if you want to check a new file extensin must be comma separated csv
# Do not include file extension, missing IPs will be saved as file-missing.csv
fileName = ''

# Master list you want to use with all the IPs that are currently being monitored
IPMasterList = 'IP-Master-List'

# List combining Interfaces and Node Polling IPs
INPlist = 'Node-And-Interface-IPs'

#--------------------------------------------------------------------

# reads in the csv
# use pd.read_csv("AssetsExport.csv", sep = "\t") to change delemiter
newAssets = pd.read_csv(fileName + '.csv')

# Sets the csv index to the IP address
newAssets.set_index("Address", inplace= True)

# read the file that contains all assets saved in solarwinds
totalAssets = pd.read_csv(IPMasterList + '.csv')

# prints the first 5 rows of the csv not counting the header
# print(totalAssets.head())

# Replaces the index from 0 to x with whatever column you specify
totalAssets.set_index("IPAddress", inplace= True)
# print(data.iloc[10])

# use pd.read_csv("AssetsExport.csv", sep = "\t") to change delemiter
ListNodes = pd.read_csv(INPlist + '.csv')

# Sets the csv index to the IP address
ListNodes.set_index("IP Address", inplace= True)

#print(data.index)
#print(data.index.str.contains(''))
#print(data)

data = pd.DataFrame()
match = False

print('The missing IPs will be saved as: ' + fileName + '-missing.csv')
print('Comparing lists...')

# Hostname of IPs that don't match
hostname = ''
# OS from scanner
OS = ''

# Iterate through list of assets in the new csv
for i in range(len(newAssets.index)):
    match = False
    scannedIP = newAssets.index[i]
    hostname = newAssets.iloc[i]['Name']
    OS = newAssets.iloc[i]['Operating System']


    # Iterates through existing list looking for matches
    for k in range(len(totalAssets.index)):
        existingIP = totalAssets.index[k]
        
        if scannedIP == existingIP:
            # If a IP in the master ip list matches 
            match = True
            break
    if match != True:
        # Iterates through existing list looking for matches
        for k in range(len(ListNodes.index)):
            existingIP = ListNodes.index[k]
            if scannedIP == existingIP:
                # If a IP in the master ip list matches 
                match = True
                break
    # If there is not a match append the IP to data which is the list that will be exported
    if match != True:
        data = data.append([{"Address":scannedIP,"Scanned HostName":hostname,"Scanned OS":OS}])


print('\nSample of missing IPs...\n')
print(data.head())
print('\nThe IPs have been compared')
print('Number of IPs compared: ' + str(len(newAssets.index)))
data.set_index("Address", inplace= True)
print('Total number of discrepencies: ' + str(len(data.index)))
data.to_csv(fileName + '-missing.csv', mode = 'w', index=True, encoding='utf-8-sig')
