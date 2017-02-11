#!/usr/bin/python
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import nmap
 

def scan_snmp():
	output=open("../outputs/snmp.dat","w")
	with open("../inputs/snmphost.dat") as f:
		print "Getting HostList from snmphost.dat file"
		servers = f.readlines()				
	for host in servers:
		
		p=sr1(IP(src="192.168.1.40",dst=host.strip())/UDP(sport=161,dport=161)/SNMP(version="v2c",community="public",PDU=SNMPget(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.2.1.1.1.0"))])),timeout=3)
		if not p:
			output.write("IP Address:"+host.strip()+" SNMP Server could not find\n")
		else:
			output.write("IP Address:"+host.strip()+" SNMP Server found!\n")
	print "Scan Finished.."

