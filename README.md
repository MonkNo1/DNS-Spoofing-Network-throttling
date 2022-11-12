"# DNS-Spoofing-Network-throttling" 

For Arp Spoofing :
Basic Installization are scapy :
```
pip3 install scapy
```
And in Attacker Machine the command need to executed : 
```
sudo su
echo 1 > /proc/sys/net/ipv4/ip_forward
```
Then Run Arp spoof bye :
```
sudo python arp_spoof.py
```

```
pip install cython
git clone https://github.com/oremanj/python-netfilterqueue
cd python-netfilterqueue
pip install .
```
