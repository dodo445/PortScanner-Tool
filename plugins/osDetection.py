#!/usr/bin/python
from scapy.all import *
import nmap 
import sys

def os_detection(host):
	nm = nmap.PortScanner()
	nm.scan(host, arguments="-O")
	

	if nm[host].has_key('osmatch'):
		output = open("../outputs/osfingerprint.dat","w")
		for osmatch in nm[host]['osmatch']:
			print('osmatch.name : {0}'.format(osmatch['name']))
			output.write('osmatch.name : {0}'.format(osmatch['name'])+"\n")
			print('osmatch.accuracy : {0}'.format(osmatch['accuracy']))
			output.write('osmatch.accuracy : {0}'.format(osmatch['accuracy'])+"\n")
			print('osmatch.line : {0}'.format(osmatch['line']))
			output.write('osmatch.line : {0}'.format(osmatch['line'])+"\n")
			print('')
			

def os_fingerP():
	with open("../outputs/open_ports.dat") as f:
		hosttext = f.readlines()
		host = ""
		output=open("../outputs/open_ports.dat",'w')
		for line in hosttext:
			if "IP Address" in line:
				output.write(line)
				host = line.split(':')[1]
				os_detection(host.strip())			

		print str(len(hosttext))+" Host Is Scanned"

