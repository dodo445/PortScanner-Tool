#! /usr/bin/python
 
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
 

def detect_firewall(dst_ip,port):
    dst_port = int(port)
    src_port = RandShort()
    ack_flag_scan_resp = sr1(IP(dst=dst_ip)/TCP(dport=dst_port,flags="A"),timeout=10)
    if (str(type(ack_flag_scan_resp))=="<type 'NoneType'>"):
		return True
    elif(ack_flag_scan_resp.haslayer(TCP)):
        if(ack_flag_scan_resp.getlayer(TCP).flags == 0x4):
            return False
        elif(ack_flag_scan_resp.haslayer(ICMP)):
            if(int(ack_flag_scan_resp.getlayer(ICMP).type)==3 and int(ack_flag_scan_resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
                return True
def firewall_hostcheck():
	with open("../outputs/open_ports.dat") as f:
		hosttext = f.readlines()
		host = ""
		output=open("../outputs/wall.dat",'w')
		for line in hosttext:
			if "IP Address" in line:
				 host = line.split(':')[1]
				 output.write(host)
			elif "Open" in line:
				port=line.split()[0]
				result = detect_firewall(host.strip(),port)
				if(result):
					output.write("Firewall Detected On Port "+port+"\n")
				else:
					output.write("NO Firewall Detected On Port "+port+"\n")

