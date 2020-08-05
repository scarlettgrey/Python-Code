import requests
import sys

url = sys.argv[1]
ext = sys.argv[2]

f1 = open("D:/Python_lat/Python/SvnDigger/all.txt","r+")

for i in range(500):
    word = f1.readline().strip()
    temp = url + "/" + word + ext
    respone = requests.get(temp)
    if respone.status_code == 200:
        print("[V] Found " + temp)
    else :
        print("[X] Not Found " + temp)