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

# Pre-condition: Ran ZMAP to scan internet:
# zmap -p 80 -o results.csv -b blacklist.txt -t 7200
# --output-filter="success = 1 && repeat = 0"

# Read zmap scan results file
networks = csv.reader(
    open(
        'results.csv',
        newline=''),
    delimiter=' ',
    quotechar='|')

subdirectory = "today" + "-network"
try:
    os.mkdir(subdirectory)
except Exception:
    pass

# Validate IP Address before accessing attributes


def valid_ip(address):
    try:
        socket.inet_aton(address)
        return address
    except BaseException:
        return False


for row in networks:
    net_row = row[0]  # Get IP address value
    obj = IPWhois(net_row)  # Create IPWhois object for each row (IP address)
    result = obj.lookup_rdap(depth=1)  # Look up whois on IP
    if valid_ip(result):
        this_net = result['network']['cidr']  # Get CIDR range of network
        # Create network object and coerce host bits to zero
        net = ipaddress.ip_network(this_net, strict=False)
        # print(this_net)  # Identify network
        net_ips = net.num_addresses
        # print(net_ips)  # Identify number of IP addresses per network

        net_array = []
        hosts = net.hosts()
        for row in hosts:
            # Coerce object to string that the other module will accept
            net_array.append(str(row))
            # print(net_array)

        # Write host as new line in each network file
        filename = net_row + '.txt'
        with open(os.path.join(subdirectory, filename), 'w') as txtfile:
            for x in net_array:
                txtfile.write(x + '\n')
            txtfile.close()
