#! /usr/bin/python
from utils import IP_Parser,port_Parser # Inludes helper methods . in file core/
from port_identify import scan_host
def check_web():
	host_list = []
	with open("../inputs/webserver.dat") as f:
		print "Getting WebList from webserver.dat file"
		webservers = f.readlines()
		output=open("../outputs/web.dat",'w')		
	for webserver in webservers:
		ip = IP_Parser(webserver.strip())
		if not ip:
			continue
		print ip
		host_list.append(IP_Parser(ip))
	scan_host(host_list,port_Parser("TOP"),'T',"../outputs/web.dat")
	print "Scan Finished..."
