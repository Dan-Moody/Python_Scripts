import requests
import hashlib

s = requests.session()
r = s.get("http://docker.hackthebox.eu:47729")
#print(r.text)
hashstr = r.text
print(hashstr.split('<h3 align=\'center\'>')[1].split('</h3>')[0])

m = hashlib.md5(hashstr.split('<h3 align=\'center\'>')[1].split('</h3>')[0].encode('utf-8'))
print(m.hexdigest())
hass = m.hexdigest()
#print(hass)
r = s.post('http://docker.hackthebox.eu:47729', data={'hash':hass})
print(r.text)
