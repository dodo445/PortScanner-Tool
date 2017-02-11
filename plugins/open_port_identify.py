#!/usr/bin/python
# -*- coding: utf-8 -*-
# DOĞUKAN UÇAK - CE 340 HOMEWORK 3
# PORT SCAN - CHECKS OPEN PORTS AND SERVICES
# SAVE THE RESULT IN open.ports.dat 

from port_identify import TcpScan

def openportidentify():
	print "Start Scan..."
	Sport = 6666
	with open("../outputs/ports.dat") as f:
		porttext = f.readlines()
		host = ""
		output=open("../outputs/open_ports.dat",'w')
		for line in porttext:
			if "IP Address" in line:
				output.write(line)
				host = line.split(':')[1]				
			elif "Scan" in line:
				pass
			elif "Open" in line:
				port=int(line.split()[0])
				result = TcpScan(host.strip(),port,Sport)
				output.write(str(port)+" "+result+" "+line.split()[1]+"\n")
				
	print "SAVED IN open_ports.dat"			
