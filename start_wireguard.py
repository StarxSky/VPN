import os 
import sys 
import subprocess
import time 

if input("Config Wireguard (1) || Restart Wireguard (2) \n") == "1":
    print("Initializing WireGuard VPN setup...")
    
    #os.system("sudo sed -i 's/^net.ipv4.ip_forward=.*/net.ipv4.ip_forward=1/' /etc/sysctl.conf") # enable ipv4 forwarding
    #os.system("sudo sed -i 's/^net.ipv6.conf.all.forwarding=.*/net.ipv6.conf.all.forwarding=1/' /etc/sysctl.conf") # enable ipv6 forwarding
    
    os.system("sudo sysctl -p") # apply sysctl changes
    os.system("sysctl net.ipv4.ip_forward=1")
    os.system("sysctl net.ipv6.conf.all.forwarding=1")
    
    os.system("chmod +x wireguard_install.sh") # make the install script executable
    time.sleep(2)
    os.system("sudo ./wireguard_install.sh")
    print("流量转发开启状态")
    os.system("sysctl net.ipv4.ip_forward=1")
    os.system("sysctl net.ipv6.conf.all.forwarding=1")

else :
    print("Starting WireGuard VPN...")
    print("Shut down Wireguard......")
    os.system("sudo wg-quick down wg0")
    print("Restarting Wireguard......")
    os.system("sudo systemctl enable wg-quick@wg0")
    os.system("sudo wg-quick up wg0")
    print("🚀 WireGuard VPN restarted successfully.")
    print("Current WireGuard status:")
    os.system("wg show")


"""
# 使用步骤
* step1 : sudo ./wireguard_install.sh
* step2 : chmod +x wireguard-install.sh
* step3 : sudo ./wireguard-install.sh
（注意开启默认的端口进站许可 UDP通讯协议）
* step4 : sudo vim /etc/sysctl.conf 
* step4 : net.ipv4.ip_forward=1
          net.ipv6.conf.all.forwarding=1
* step5 : sudo sysctl -p
* step6 : 设置开机自启：`sudo systemctl enable wg-quick@wg0`
* step7 : 激活wg0的接口：`sudo wg-quick up wg0`
"""
