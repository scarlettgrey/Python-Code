import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 11111
s.bind((host,port))
s.listen(5)
savedimana = 'D:/'

while True:
    con, addr = s.accept()
    print(str(addr) + "has Connected")
    i = 1
    f = open(savedimana + 'file_' + str(i) + '.txt','wb')
    i = i + 1
    print("Saving File...")
    a = 0
    l = con.recv(1024)
    while l:
        print(a)
        f.write(l)
        l = con.recv(1024)
        a += 1
    print("Done saving file...")
f.close()
con.close()
s.close()
