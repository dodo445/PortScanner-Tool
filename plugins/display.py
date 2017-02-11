#!/usr/bin/python

def display_all():
	print "Displaying Output Files...."
	print "*****icmp.dat FILE******"
	with open("../outputs/icmp.dat") as f:
		println(f.readlines())
	print "******ports.dat FILE******"
	with open("../outputs/ports.dat") as f:
		println(f.readlines())
	print "******open_ports.dat FILE*******"
	with open("../outputs/open_ports.dat") as f:
		println(f.readlines())
	print "******wall.dat FILE******"
	with open("../outputs/wall.dat") as f:
		println(f.readlines())
	print "*****web.dat FILE******"
	with open("../outputs/web.dat") as f:
		println(f.readlines())
	print "******snmp.dat FILE*****"
	with open("../outputs/snmp.dat") as f:
		println(f.readlines())
	print "Displaying Input Datas"
	print "******webserver.dat FILE*****"
	with open("../inputs/webserver.dat") as f:
		println(f.readlines())
	print "*****snmphost.DAT FILE******"
	with open("../inputs/snmphost.dat") as f:
		println(f.readlines())
	 
		
def println(lines):
	for line in lines:
		print line


