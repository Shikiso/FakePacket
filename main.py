from scapy.all import sniff, Ether

interface = "lo"
count = 1

def handle(packet):
    print(packet.show())

sniff(iface=interface, count=count, prn=handle)
