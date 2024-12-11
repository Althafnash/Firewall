from scapy.all import sniff, IP, TCP, UDP,get_if_list
import threading

# Example rules
ALLOWED_IPS = ['192.168.1.10']
BLOCKED_PORTS = [80, 443]

class Firewall():
    def __init__(self, output_callback):
        self.output_callback = output_callback
        self.sniffing = False
        self.sniff_thread = None
    
    def packet_callback(self,packet):
        # Check if the packet has an IP layer
        if IP in packet:
            ip_src = packet[IP].src
            ip_dst = packet[IP].dst

            # Allow packets from ALLOWED_IPS
            if ip_src in ALLOWED_IPS:
                self.output_callback(f"Allowed packet from {ip_src} to {ip_dst}")
                return

            if TCP in packet or UDP in packet:
                sport = packet[TCP].sport if TCP in packet else packet[UDP].sport
                dport = packet[TCP].dport if TCP in packet else packet[UDP].dport

                if sport in BLOCKED_PORTS or dport in BLOCKED_PORTS:
                    self.output_callback(f"Blocked packet from {ip_src} to {ip_dst} on port {sport if sport in BLOCKED_PORTS else dport}")
                    return

            self.output_callback(f"Allowed packet from {ip_src} to {ip_dst}")

    def start_firewall(self, interface):
        if self.sniffing:
            return
        self.output_callback(f"Starting firewall on {interface}\n")
        self.sniffing = True
        self.sniff_thread = threading.Thread(target=self.sniff_packets, args=(interface,))
        self.sniff_thread.start()

    def stop_firewall(self):
        if self.sniffing:
            self.sniffing = False
            self.sniff_thread.join()
            self.output_callback("Firewall stopped.\n")

    def start_scan(self):
        interfaces = get_if_list()
        self.output_callback("Available interfaces:")
        for i, iface in enumerate(interfaces):
            self.output_callback(f"{i}: {iface}")

    def sniff_packets(self, interface):
        sniff(prn=self.packet_callback, store=0, stop_filter=lambda x: not self.sniffing)