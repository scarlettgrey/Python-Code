import hashlib
import requests
from bs4 import BeautifulSoup

s = requests.Session()
x = s.get('http://docker.hackthebox.eu:31265/')
soup = BeautifulSoup(x.content,'html.parser')
letter = str(soup.find('h3'))

a = letter[19:39]
result = hashlib.md5(a.encode())
values = {
    'hash' : result.hexdigest()
}

a = s.post('http://docker.hackthebox.eu:31265/',data=values)
soupa = BeautifulSoup(a.content,'html.parser')
print(soupa)
