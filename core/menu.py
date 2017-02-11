#!/usr/bin/python
# -*- coding: utf-8 -*-
# DOĞUKAN UÇAK - CE 340 HOMEWORK 3
# Main Menu Provides User To Use Plugins

import utils
import sys
from sys import path
path.append("../plugins/")
import os
import string
from icmp_ping import checkhost
from port_identify import portIdentify
from open_port_identify import openportidentify
from firewall import firewall_hostcheck
from webserver import check_web
from syn_flood import syn_flood
from osDetection import os_fingerP
from snmp import scan_snmp
from display import display_all

clear = lambda: os.system('clear') #on Linux System Clear Terminal

print "DOGUKAN UCAK HOMEWORK 3 - BUILDING SIMPLE TOOLS"
def printMenu():
	print "CHOOSE WHICH OPERATION YOU WANT USE"
	print "1) ICMP PING: FIND ALIVE HOSTS "
	print "2) PORT IDENTIFICATION"
	print "3) OPEN PORT IDENTIFICATION"
	print "4) OS FINGERPRINT IDENTIFICATION"
	print "5) FIREWALL&ROUTER IDENTIFICATION"
	print "6) WEB SERVER DETECTION"
	print "7) SNMP DETECTION"
	print "8) SYN_FLOOD"
	print "9) DISPLAY OUTPUTS"
	print "CTRL-C TO QUIT..."
	selection =raw_input("ENTER YOUR SELECTION:")
	return selection
def operationSelector(selection):
	if(selection == '1'):
		icmp()
	elif(selection == '2'):
		port_scan()
	elif(selection == '3'):
		open_port_scan()
	elif(selection == '4'):
		os_fingerprint()
	elif(selection == '5'):
		firewallcheck()
	elif(selection == '6'):
		webserver_check()
	elif(selection == '7'):
		scan_snmp()
	elif(selection == '8'):
		syn_attack()
	elif(selection == '9'):
		display()
		pass
	else:
		print "YOU ENTERED INVALID SELECTION!"
	prompt = raw_input("ENTER 1 TO BACK TO MENU OR ANY KEY TO QUIT:")
	
	if(prompt == '1'):
		clear()
		operationSelector(printMenu())
	
	else:
		print "QUITTING..."
		sys.exit(0)
def icmp():
	while(True):
		ip_list = raw_input("ENTER IP OR IP RANGE:").strip() 
		if(checkhost(ip_list) == "INVALID"):
			print "INVALID INPUT , PLEASE SPECIFY A VALID IP ADRESS OR RANGE"
		else:			
			break;
def port_scan():	
		port_range = raw_input("PLEASE SPECIFY PORT RANGE:")
		scantype = raw_input("ENTER T FOR TCP SCAN , S FOR SYN SCAN , F FOR FIN SCAN TOP FOR TOP PORTS:")
		portIdentify(port_range,str(scantype).strip())
def open_port_scan():
	openportidentify();
def os_fingerprint():
	os_fingerP()
def firewallcheck():
	firewall_hostcheck()
def webserver_check():
	check_web()
def syn_attack():
	ip = raw_input("Enter IP Adress To Syn Flood:")
	syn_flood(ip,80,10000)
def snmp_detect():
	scan_snmp()
def display():
	display_all()
def main():
	while(True):
		operationSelector(printMenu())		
try:
    main()
except KeyboardInterrupt:
	print '\nQuitting....'
	sys.exit(0)
