#!/usr/bin/python
# -*- coding: utf-8 -*-
# DOĞUKAN UÇAK - CE 340 HOMEWORK 3
# ICMP PING SCAN - CHECKS IF THE HOST IS ALIVE OR NOT
# Ping an IP range and collect IP adresses of the hosts that are alive and save 
# the result in a text file, call this icmp.dat
# Usage icmp_ping.py <IP Range>
import logging 
logging.getLogger("scapy.runtime").setLevel(logging.ERROR) # To disable unnecessary warnings coming from Scapy
import sys
from sys import path
path.append("../core/")
from scapy.layers.inet import ICMP,IP
from utils import IP_Parser # Inludes helper methods . in file core/
from scapy.all import *

def checkhost(ipaddress):
	print "START RUNNING ICMP PING HOST CHECK.."  
	host_ip = IP_Parser(ipaddress)
	if(host_ip==False):		
		return "INVALID"
	host_list = []
    # Send ICMP ping request, wait for answer
	if isinstance(host_ip, list):
		for host in host_ip:
			resp = sr1(IP(dst=str(host)) / ICMP(), timeout=2, verbose=0)
			if (str(type(resp)) == "<type 'NoneType'>"):
				print str(host) + " is down or not responding."
			elif (int(resp.getlayer(ICMP).type) == 3 and int(resp.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]):
				print str(host) + " is blocking ICMP."
			else:
				print str(host) + " is responding."
				host_list.append(host)
		print "Out of " + str(len(host_ip)) + " hosts, " + str(len(host_list)) + " are online."
		output=open("../outputs/icmp.dat",'w')
		for host in host_list:
			output.write(str(host)+"\n")
		print ("Results were written to icmp.dat file in outputs directory")
		return host_list
	else:
		output=open("../outputs/icmp.dat",'a')
		resp = sr1(IP(dst=str(host_ip)) / ICMP(), timeout=2, verbose=0)
		if (str(type(resp)) == "<type 'NoneType'>"):
			print str(host_ip) + " is down or not responding."
			return False
		elif (int(resp.getlayer(ICMP).type) == 3 and int(resp.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]):
			print str(host_ip) + " is blocking ICMP."
			return False
		else:
			print str(host_ip) + " is responding."
			output.write(str(host_ip)+"\n")
			return True
	
		
	
	


	


