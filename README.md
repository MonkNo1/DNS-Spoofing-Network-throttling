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

for Running DNS spoofing :

We need NetFilterqueue: 

For Installization:
Installaztion of  NetFiltersQueue : ```https://github.com/johnteslade/python-netfilterqueue```
```
apt-get install build-essential python-dev libnetfilter-queue-dev
pip install NetfilterQueue
```
OR
```
pip install cython
git clone https://github.com/oremanj/python-netfilterqueue
cd python-netfilterqueue
pip install .
```

After installing that Run the ARP Spoofer and Run This Dns Spoofer Spoofing 
```
python3 cache.py
```

