import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

localhost = '127.0.0.1'
s.connect((localhost,50505))
nama = input("Masukkan nama anda: ")
s.sendall(nama.encode())
while 1:
    pesan = input(nama + ":")
    if pesan != "":
        if pesan == "#exit":
            pesan = " telah meninggalkan obrolan"
            s.sendall(pesan.encode())
            break
        s.sendall(pesan.encode())
        a = s.recv(1024)
        A = a.decode()
        print("\nServer: " + A)
s.close()