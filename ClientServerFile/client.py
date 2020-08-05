import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 11111
s.connect((host,port))

cwd = os.getcwd()
files = os.listdir(cwd)

#file yang mau di input
f = open('D:/Python_lat/ClientServerFile/haha.txt','rb')
l = f.read(1024)
while l:
    s.send(l)
    l = f.read(1024)

s.close()