#!/usr/bin/python
import os.path
import datetime
import ipaddress
import subprocess
import csv
import ipwhois
import re

from ipwhois import IPWhois
from pprint import pprint
from IPy import IP

# 1. Ran ZMAP to scan internet:
# zmap -p 80 -o results.csv -b blacklist.txt -t 7200 --output-filter="success = 1 && repeat = 0"

# READ ZMAP SCAN RESULTS FILE
networks = csv.reader(open('results.csv', newline=''), delimiter=' ', quotechar='|')

# CREATE SUBDIRECTORY
subdirectory = "today" + "-network"
try:
    os.mkdir(subdirectory)
except Exception:
    pass

# VALIDATES IP ADDRESS
def valid_ip(address):
    try:
        socket.inet_aton(address)
        return address
    except:
        return False

for row in networks:
    # NETWORK OBJECT
    net_row = row[0] # Gets IP address value
    obj = IPWhois(net_row) # Creates IPWhois object for each row (IP address)

    result = obj.lookup_rdap(depth=1) # Looks up whois on IP
    if valid_ip(result):
        this_net = result['network']['cidr'] # Gets CIDR range of network
        net = ipaddress.ip_network(this_net, strict=False) # Creates network object and coerces host bits to zero
        print(this_net) # Identify network
        net_ips = net.num_addresses
        print(net_ips) # Identify number of IP addresses per network

        # COLLECT HOSTS
        net_array = []
        hosts = net.hosts()
        for row in hosts:
            net_array.append(str(row)) # Coerce object to string that the other module will accept
            #print(net_array)

        # WRITE TO FILE
        filename = net_row + '.txt'
        with open(os.path.join(subdirectory, filename), 'w') as txtfile:
            for x in net_array:
                txtfile.write(x + '\n')
            txtfile.close()
