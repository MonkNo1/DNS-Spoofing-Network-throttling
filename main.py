import tkinter as tk
import cache
import arp

def thr():
    a = e1.get()
    cache.DnsSnoof()

win=tk.Tk()
l1=tk.Label(text="SASTRA UNIVERSITY")
l1.pack()
l2=tk.Label(text="DNS SPOOFING AND NETWORK THROTTLING")
l2.pack()
k1=tk.Label(text="Host IP:")
k1.pack()
e1=tk.Entry()
e1.pack()

# a = e1.get()

k2=tk.Label(text="GateWay")
k2.pack()
e2=tk.Entry()
e2.pack()

k2=tk.Label(text="SpoofIP")
k2.pack()
e2=tk.Entry()
e2.pack()


t1=tk.Label(text="network throttling:")
t1.pack()
b1=tk.Button(text="Start") #commad = thr()
b2=tk.Button(text="Stop")
b1.pack()
b2.pack()
t2=tk.Label(text="ARP Spoofing:")
t2.pack()
b3=tk.Button(text="Start")
b4=tk.Button(text="Stop")
b3.pack()
b4.pack()
t3=tk.Label(text="DNS Spoofing:")
t3.pack()
b5=tk.Button(text="Start")
b6=tk.Button(text="Stop")
b5.pack()
b6.pack()


name=tk.Label(text="R.Chandrakumar")
name.pack()
win.minsize(400,400)
win.mainloop()