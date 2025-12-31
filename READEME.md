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