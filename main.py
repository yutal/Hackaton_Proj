from scapy.all import get_if_addr,conf,get_if_hwaddr,get_iface_mode
# IP = get_if_addr(conf.iface)
IP = get_if_hwaddr("eth1")
print(IP)
