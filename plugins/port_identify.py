#!/usr/bin/python
# -*- coding: utf-8 -*-
# DOĞUKAN UÇAK - CE 340 HOMEWORK 3
# PORT SCAN - CHECKS OPEN PORTS AND SERVICES
# SAVE THE RESULT IN ports.dat 
# Usage port_identify.py <IP Range>
import sys
from sys import path
path.append("../core/")
import utils
from utils import IP_Parser,getServiceName # Inludes helper methods . in file core/
import time
import logging
logging.getLogger("scapy.runtime").setLevel(logging.CRITICAL)
from scapy.all import *
import sys
from sys import path
path.append("../core/")
from utils import IP_Parser,port_Parser # Inludes helper methods . in file core/




 
def TcpScan(host,port,Sport): # Standart Tcp Port Scan - Sends Syn , if RST answer got , it means the port is closed
	
	tcp_scan = sr1(IP(dst=host)/TCP(sport=Sport,dport=port,flags="S"),timeout=2)
	if(str(type(tcp_scan))=="<type 'NoneType'>"):
		return "Closed"
	elif(tcp_scan.haslayer(TCP)):
		if(tcp_scan.getlayer(TCP).flags == 0x12):
			send_rst = sr(IP(dst=host)/TCP(sport=Sport,dport=port,flags="AR"),timeout=1)
			return "Open"
		elif (tcp_scan.getlayer(TCP).flags == 0x14):
			return "Closed"
def SynScan(host,port,source_port): # Syn Scan , It is slower than regular tcp scan , but it is less detectable , Again Sends Syn , But reply Syn+Ack with RST
	
	syn_scan = sr1(IP(dst=host)/TCP(sport=source_port,dport=port,flags="S"),timeout=10)
	if(str(type(syn_scan))=="<type 'NoneType'>"):
		print "Filtered"
	elif(syn_scan.haslayer(TCP)):
		if(syn_scan.getlayer(TCP).flags == 0x12):
			send_rst = sr(IP(dst=host)/TCP(sport=source_port,dport=port,flags="R"),timeout=10)
			print "Open"
		elif (syn_scan.getlayer(TCP).flags == 0x14):
			print "Closed"
		elif(syn_scan.haslayer(ICMP)):
			if(int(syn_scan.getlayer(ICMP).type)==3 and int(syn_scan.getlayer(ICMP).code) in [1,2,3,9,10,13]):
				print "Filtered"

def FinScan(host,port):
	
	fin_scan = sr1(IP(dst=host)/TCP(dport=port,flags="F"),timeout=10)
	if (str(type(fin_scan))=="<type 'NoneType'>"):
		print "Open|Filtered"
	elif(fin_scan.haslayer(TCP)):
		if(fin_scan.getlayer(TCP).flags == 0x14):
			print "Closed"
		elif(fin_scan.haslayer(ICMP)):
			if(int(fin_scan.getlayer(ICMP).type)==3 and int(fin_scan.getlayer(ICMP).code) in [1,2,3,9,10,13]):
				print "Filtered"

def scan_host(host_list,port_range,scantype,filename):
	Sport = int(RandShort())
	output=open(filename,'w')
	if isinstance(host_list, list):
		
		for host in host_list:		
			output.write("IP Address:"+str(host)+"\n")			
			if(scantype=='T'):
				for port in port_range:
					result=TcpScan(host.strip(),port,Sport)
					if not result:
						continue
					output.write(str(port)+" "+str(getServiceName(port))+" "+result+"\n")
				output.write("(TCP)Scan Time:"+time.strftime("%H:%M:%S")+"\n")
			elif(scantype=='S'):
				for port in port_range:
					result=SynScan(host,port,Sport)
					output.write(str(port)+" "+str(getServiceName(port))+" "+result+"\n")								
				output.write("(SYN)Scan Time:"+time.strftime("%H:%M:%S")+"\n")	
			elif(scantype=='F'):
				for port in port_range:
					result=FinScan(host,port,Sport)				
					output.write(str(port)+" "+str(getServiceName(port))+" "+result+"\n")				
				output.write("(FIN)Scan Time:"+time.strftime("%H:%M:%S")+"\n")
			

def portIdentify(portrange,scanType): # Scans host given from the file
	print "START SCANNING HOST IN icmp.dat"
	tic = time.time() 
	with open("../outputs/icmp.dat") as f:
		ip_list = f.readlines()
		alive_list = []
		for ip in ip_list:
			icmp = IP(dst=ip)/ICMP()
			resp = sr1(icmp, timeout=10)
			if not resp:
				alive_list.append(ip)
			print "SCANNING PORTS: "+str(port_Parser(portrange))
		scan_host(alive_list,port_Parser(portrange),scanType,"../outputs/ports.dat")
	print "SCAN FINISHED IN "+str(time.time()-tic)+"s"	

