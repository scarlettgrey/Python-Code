import socket
import _thread

kataterlarang = ["root","alert","script","sys"]

def fromclienttoserver(conn,addr):
    p.connect((ip,45464))
    p.sendall(namaclient)
    while True:
        data = conn.recv(1024)
        if len(data) <= 20:
            if data.decode()  not in kataterlarang:
                p.sendall(data)
            else:
                conn.sendall("Jangan aneh-aneh".encode())
                conn.close()
                break
        else:
            conn.sendall("File/sesuatu yang hendak dikirim melebihi batas".encode())
            p.sendall(" ".encode())
        data1 = p.recv(1024)
        conn.sendall(data1)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
p = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip = '127.0.0.1'
s.bind((ip,50505))
s.listen(5)

while True:
    conn, addr = s.accept()
    print("Received Connection from " + str(addr))
    namaclient = conn.recv(1024)
    print("Forwarding Connection to Server")
    _thread.start_new_thread(fromclienttoserver,(conn,addr))