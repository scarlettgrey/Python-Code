import socket
import _thread
from threading import Thread

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

localhost = '127.0.0.1'
s.bind((localhost,45464))
s.listen(5)

def server(conn,addr):
    nama_client = conn.recv(1024).decode()
    print("Welcome " + nama_client + " To Chat")
    while True:
        data = conn.recv(1024).decode()
        print(nama_client + ":" +data)
        if not data:
            break
        a = input("Server: ")
        A = a.encode()
        s = conn.sendall(A)

print("Server is Started")
while True:
    conn, addr = s.accept()
    print("Received Connection From " + str(addr))
    _thread.start_new_thread(server,(conn,addr))
        
conn.close()