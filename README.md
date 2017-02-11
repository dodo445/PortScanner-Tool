DOGUKAN UCAK Simple Port Scanner Tool - HOW TO USE
YOU HAVE TO BE ROOT TO RUN THE SCRIPT
1) IN THE PROMPT MENU , YOU CAN CHOOSE ANY OPERATION YOU WANT, FOR THE FIRST USAGE, YOU SHOULD CHOOSE 1 OPERATION TO FILL YOUR icmp.dat WHICH WILL INCLUDE YOUR ALIVE HOST -- see firstlook.png
2)USAGE FOR ICMP.PY -- icmp.py <IP or RANGE> # You can specify IP RANGE like; 192.168.1.1 , 192.168.1.1,2,3 or 192.168.1.1-50, also a domain name ex: www.google.com.tr -- see icmp.png
3)2nd OPTION MAKE A PORT SCAN ON THE TARGEST IN icmp.dat file , you can specify port range like: 20-50
YOU CAN ALSO ENTER "TOP" TO SCAN top popular ports and enter your scan type
4)3nd OPTION IS CHECK FOR THE OPEN PORTS from port.dat file and if they are still open , writes down to open_ports.dat
5)4TH OPTION IS TRY TO GUESS OPERATING SYSTEM OF TARGET HOST , I USED NMAP MODULE TO DO THIS
6)5TH IS CHECK IF THE TARGET HOSTS AND PORT HAS A FIREWALL
7)6TH WEBSERVER DETECTION , READS domain names from inputs/webservers.dat file and scan them for ports and services. You can modify more domain names to webservers.dat files
8)7TH SNMP DETECTION , READS HOST IP ADDRESSES FROM inputs/snmphosts.dat file and scan them for snmp server
9)8TH SYN_FLOOD ATTACK ON TARGET MACHINE
10) LAST OPTION JUST DISPLAYS INPUT AND OUTPUT FILES

YOU ONLY NEED TO FOLLOW THE USER PROMPT , IT WILL SHOW YOU SIMPLY HOW TO USE , WHEN YOU ARE DONE WITH AN OPERATION YOU CAN GO BACK TO MAIN MENU AND TRY ANOTHER OPERATION.
