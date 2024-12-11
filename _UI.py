import tkinter as tk 
from tkinter import font
from Firewall_UI import NashFirewallApp
from interface_UI import Interfaces
from YARA_UI import YARA

root = tk.Tk()
root.title("Nash_Firewall")
root.geometry("1000x1000")
custom_font = font.Font(family="Helvetica", size=20) 

def open_YARA_window():
    firewall_window = tk.Toplevel()  
    firewall_window.title("Nash Firewall")
    firewall_window.geometry("800x600")
    firewall_app = YARA(root=firewall_window) 

def open_firewall_window():
    firewall_window = tk.Toplevel()  
    firewall_window.title("Nash Firewall")
    firewall_window.geometry("800x600")
    firewall_app = NashFirewallApp(root=firewall_window) 

def open_Interface_window():
    Interface_window = tk.Toplevel()  
    Interface_window.title("Nash Interface")
    Interface_window.geometry("800x600")
    Interface_app = Interfaces(root=Interface_window) 

tk.Label(root, text="Welcome to Nash Firewall", font=custom_font).grid(row=1, column=0, padx=75, pady=10)

tk.Label(root, text="Nash Firewall", font=custom_font).grid(row=2, column=0, padx=75, pady=10)

text = "'Nash Firewall' is a network security application designed to protect your network from unauthorized access and malicious activities. It operates as a software-based firewall solution implemented in Python, leveraging the capabilities of the Scapy library for packet sniffing and manipulation."
tk.Label(root, text=text,wraplength=600, font=custom_font).grid(row=3, column=0, padx=10, pady=10 )

tk.Label(root, text="Click on any of the following buttons to start the Firewall services ", font=custom_font).grid(row=4, column=0, padx=75, pady=10)

buttons_frame = tk.Frame(root)
buttons_frame.grid(row=5, column=0, columnspan=2, pady=10, sticky="ew")

start_button = tk.Button(buttons_frame, text="Firewall", command=open_firewall_window, font=custom_font)
start_button.pack(side=tk.LEFT, padx=10)

stop_button = tk.Button(buttons_frame, text="Interface", command=open_Interface_window,  font=custom_font)
stop_button.pack(side=tk.LEFT, padx=10)

stop_button = tk.Button(buttons_frame, text="Malware", command=open_YARA_window,  font=custom_font)
stop_button.pack(side=tk.LEFT, padx=10)

root.grid_rowconfigure(6, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
