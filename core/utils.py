#!/usr/bin/python
# -*- coding: utf-8 -*-
# DOĞUKAN UÇAK - CE 340 HOMEWORK 3
# Includes Helper Functions
import re
import socket
import netaddr
import sys
# utils.py , contains some helper methods to whole application 

# There are more efficient algorithms used for accepting different ways of host Ip accepting , but I wanted to try my own method to accept it
# IP_Parser method provide my application to accept IP inputs in different forms : It accepts : 192.168.1.1 , 192.168.1.1,2,3 , 192.168.1.1-50
# In addition it converts host name to ip adress by using netaddr 
# This method simply provides flexibility to accept host IP inputs
def IP_Parser(host_address): 
	ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"; # Ex: 192.168.1.1
	ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$"; # Ex: www.google.com.tr
	ValidIpRangeWithSubNet = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])[/]2[0-9]$" # Ex: 192.168.1.0/24
	ValidIpRangeWithCommas = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])([,]([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))*$" # Ex: 192.168.1.1,2,3...
	ValidIpAddressWithRange = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])[-]([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$" # Ex: 192.168.1.1-255
	if(re.search(ValidIpAddressRegex,host_address)): # Validate and return a single ip adress
		return host_address
	elif(re.search(ValidHostnameRegex,host_address)):
		try:
			return socket.gethostbyname(host_address)
		except Exception:
			return False # Returning false means an error is occured while geting the Ip Adresss
	elif(re.search(ValidIpRangeWithSubNet,host_address)):
		try:
			return netaddr.IPNetwork(host_address)
		except Exception:
			return False # Returning false means an error occured while converting the host list
	elif(re.search(ValidIpRangeWithCommas,host_address)): # Ip adresses like 192.168.1.1,2,3,4.. are proccessed here
		host_list = [] 
		host_address = host_address.split(",") # This splits Ex: 192.168.1.1,2,3,4 as {192.168.1.1},{1},{2},{3},{4}
		base_ip = host_address[0] # I assing the fist element of the array list as base Ip Adress
		host_list.append(base_ip) # Then add the base ip adress
		for last_octet in range(len(host_address)-1):
			host_list.append(base_ip[:-1*(len(base_ip)-base_ip.rfind(".")-1)]+host_address[last_octet+1]) # Substring operation , I just cut the last octet from base_ip and add the new octet
		return host_list
	elif(re.search(ValidIpAddressWithRange,host_address)): # Ip adresses like 192.168.1.1-20.. are proccessed here
		host_list = []
		three_octects = host_address[:-1*(len(host_address)-host_address.rfind(".")-1)]
		last_octet = host_address[host_address.rfind(".")+1:].split("-")
		for range_number in range(int(last_octet[0]),int(last_octet[1])+1):
			host_list.append(three_octects+str(range_number))
		return host_list
	else:
		return False # This means given input does not match by any of the regular expressions
def port_Parser(port_range):
	if "-" in port_range:
		p_range = port_range.split('-')
		return range(int(p_range[0]),int(p_range[1])+1)
	elif "TOP" in port_range:
		return [21,22,23,25,53,67,139,80,443,8080]		
	else:
		return range(port_range,port_range+1)
def getServiceName(port):
	service_dictionary = {'21':'FTP','22':'SSH','23':'Telnet','25':'SMTP','53':'DNS','67':'DHCP','80':'HTTP','110':'POP','135':'RPC','137':'NETBIOS','138':'NETBIOS','139':'NETBIOS','143':'IMAP','443':'HTTPS','3389':'Terminal Service'}
	try:		
		service = service_dictionary[str(port)];
	except KeyError:
		service = "Unknown"	
	return service
	




	
