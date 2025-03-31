from scapy.all import sniff, Ether, send, IP, TCP

interface = "lo"
count = 1

def handle(packet):
    packet[3].load = b"Goodbye"
    print(packet)
    send(IP(dst=packet[1].dst)/TCP(dport=packet[2].dport, flags=packet[2].flags)/"Goodbye")

sniff(iface=interface, count=count, prn=handle)
