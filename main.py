import tkinter as tk
import cache
import NetworkThrottling
import arp

#Network Throtttling 
def thrstart():
    print(a,b,c)
    NetworkThrottling.thpoint(a,b,1)

def thrstop():
    NetworkThrottling.thpoint(a,b,3)

def thrreset():
    NetworkThrottling.stop(a,b)

#ARP spoofing
def arpstart():
    arp.spoint(a,b,1)

def arpstop():
    arp.spoint(a,b,3)

def arpreset():
    arp.stop(a,b,1)

#DNS Spoofing 
def dnsstart():
    cache.dnsspoint(c,1)
def dnsstop():
    cache.dnsspoint(c,3)

win=tk.Tk()
l1=tk.Label(text="SASTRA UNIVERSITY")
l1.pack()
l2=tk.Label(text="DNS SPOOFING AND NETWORK THROTTLING")
l2.pack()

k1=tk.Label(text="Host IP:")
k1.pack()
e1=tk.Entry()
e1.pack()

k2=tk.Label(text="GateWay")
k2.pack()
e2=tk.Entry()
e2.pack()

k3=tk.Label(text="SpoofIP")
k3.pack()
e3=tk.Entry()
e3.pack()

t1=tk.Label(text="network throttling:")
t1.pack()
b1=tk.Button(text="Start",command=thrstart) #commad = thr()
b2=tk.Button(text="Stop",command=thrstop)
b3=tk.Button(text="Reset",command=thrreset)
b1.pack()
b2.pack()
b3.pack()
t2=tk.Label(text="ARP Spoofing:")
t2.pack()
b4=tk.Button(text="Start",command=arpstart)
b5=tk.Button(text="Stop",command=arpstop)
b6=tk.Button(text="Reset",command=arpreset)
b4.pack()
b5.pack()
b6.pack()
t3=tk.Label(text="DNS Spoofing:")
t3.pack()
b7=tk.Button(text="Start",command=dnsstart)
b8=tk.Button(text="Stop",command=dnsstop)
b7.pack()
b8.pack()

global a,b,c
a = e1.get()
b = e2.get()
c = e3.get()

name=tk.Label(text="R.Chandrakumar")
name.pack()
win.minsize(400,400)
win.mainloop()