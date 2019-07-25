import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import UpdateAsset as upa

# First searches for duplicate Hostnames then compares the existing IP
# connected with that hostname and updates it if the new informatin
# different. Also updates the existing csv with any information in the
# new csv.
#
# If the IP is not yet in the list create a new row with all the available
# information for it.
#


# Fixes the label for the hostname column in the new asset table
# attempts to find old hostname column and change it to fit standard
def fixHostnameLabel():
    try:
        nAssets.rename(columns={'Hostname':'Name'}, inplace=True)
    except:
        try:
            nAssets.rename(columns={'hostname':'Name'}, inplace=True)
        except:
            pass
        
    try:
        nAssets.set_index("Name", inplace= True)
    except:
        print('No value Hostname column name in the new asset csv')
        exit(0)

# Fixes the label for the IP column in the new asset table
# attempts to find old IP column and change it to fit standard
def fixIPLabel():
    try:
        nAssets.rename(columns={'IP':'Address'}, inplace=True)
    except:
        try:
            nAssets.rename(columns={'ip':'Address'}, inplace=True)
        except:
            print('No value IP address column name in the new asset csv')
            exit(0)

    

# Tries to find the right label and value for the new assets hostname
def findAssetIP():
    return nAssets.iloc[i]['Address']

# Tries to find the right label and value for the new assets hostname
def findDFIP():
    return data.iloc[k]['Address']

#--------------------------------------------------------------------

# reads in the csv
# use pd.read_csv("AssetsExport.csv", sep = "\t") to change delemiter
data = pd.read_csv('test.csv')

# read the file that you want to append to the asset list
# nAssets = new assets
nAssets = pd.read_csv('SAS.csv')

# attempts to make the headers uniform
fixHostnameLabel()
fixIPLabel()

# prints the first 5 rows of the csv not counting the header
# print(data.head())

# Replaces the index from 0 to x with whatever column you specify
data.set_index("Name", inplace= True)
# print(data.iloc[10])

#print(data.index)
#print(data.index.str.contains('10.105.7.45'))
#print(data)

# Iterate through list of assets in the new csv
for i in range(len(nAssets.index)):
    assetName = nAssets.index[i]
    h1 = findAssetIP()
    count = 0 # count for the number of matches

    # Iterates through existing list looking for matches
    for k in range(len(data.index)):
        dfName = data.index[k]
        h2 = findDFIP()

        try:
            # If the new asset does have a hostname
            assetName = assetName.lower()

            try:
            # converts the hostname to lower case so they can be compared
            dfName = dfName.lower()
            
            # This if statement needs to be made more specific eventually
            # If the HOSTNAMES are the SAME
            if assetName.split(' -')[0] == dfName.split('.')[0]:
                h2 = findDFIP()
                count += 1
        except:
            # If the entry does not have a hostname try the IP
            if h1 == h2:
                print('HERE')

            
        except:
            # If the new asset does not have a hostname


        
        
        if count == 0:
            # If the hostname is not already in the list create a new entry for it
            asset = upa.fillCellVals(nAssets.iloc[i])
            data = data.append(asset, sort=False)

print(data)
data.to_csv('test2.csv', mode = 'w', index=False, encoding='utf-8-sig')
upa.test(nAssets, data)
