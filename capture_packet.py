#!/usr/bin/env python
from scapy.all import sniff

interface = 'lo' # lo = localhost
packet_to_capture = 10

def handler(packet):
    print(packet.show())
    print("\n")

sniff(iface=interface, count=packet_to_capture, prn=handler)
