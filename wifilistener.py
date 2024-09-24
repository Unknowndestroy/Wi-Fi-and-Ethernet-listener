import os
import sys
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if __name__ == "__main__":
    if not is_admin():
        print("Adminastirator permission required. Restarting as an adminastirator...")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit(0)
    
    # Yönetici olarak çalışıyorsanız buraya kodunuzu ekleyin
    from scapy.all import sniff, IP

    def packet_handler(packet):
        if IP in packet:
            ip_src = packet[IP].src
            ip_dst = packet[IP].dst
            print(f"Source: {ip_src}, Destination: {ip_dst}")

    def start_sniffing(interface):
        print(f"Sniffing on {interface}...")
        sniff(iface=interface, prn=packet_handler, count=0)

    interface = input("Enter the interface to sniff (e.g., Ethernet, Wi-Fi): ")
    start_sniffing(interface)
