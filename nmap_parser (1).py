# Author Daniel Moody
# Get Panda library when updating this to make editing csv easier
#!/usr/bin/env python
import nmap # import nmap.py module
import csv # inport
nm = nmap.PortScanner() # instantiate nmap.PortScanner object

# Open the CSV file
f = open('nmap.csv','wb')

# If you want to do a pingsweep on network 10.13.32.0/24:
scanned_Data = nm.scan(hosts='10.13.32.0/24', arguments='-n -sP -PE -PA')


# Open the CSV file
try:
    with open('nmap.csv', 'w') as csvfile:
        fields = ['Name','Type','IPv4','MAC','Vendor','Status','Reason']
        writer = csv.writer(csvfile, lineterminator = '\n')
        writer.writerow(fields)
        
        # iterate through all the IPs that nmap found
        # Sry this code will be aweful to maintain but its mostly demo purposes
        for IP in scanned_Data['scan'].keys():
            #save hostname
            #Why the heck is hostname a list with 1 element that is a dictionary
            #name
            name = scanned_Data['scan'][IP]['hostnames'][0].get('name', 'NA')
            #type
            addr_type = scanned_Data['scan'][IP]['hostnames'][0].get('type', 'NA')

            #save addresses
            #ipv4
            ipv4 = scanned_Data['scan'][IP]['addresses'].get('ipv4', 'NA')
            #mac
            mac = scanned_Data['scan'][IP]['addresses'].get('mac', 'NA')

            #save vendor
            #&mac
            vendor = scanned_Data['scan'][IP]['vendor'].get(mac, 'NA')

            #status
            #state
            state = scanned_Data['scan'][IP]['status'].get('state', 'NA')
            #reason
            reason = scanned_Data['scan'][IP]['status'].get('reason', 'NA')

            #Write current row to csv
            writer.writerow([name,addr_type,ipv4,mac,vendor,state,reason])
            
        #Close csv
        csvfile.close()

        #Write success message
        print('CSV written successfully')
except IOError:
    print("I/O error")
