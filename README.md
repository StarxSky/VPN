# Get more safty VPN ? (AmneziaWG)
```
$ chmod +x amneziawg-install.sh
$ ./amneziawg-install.sh

Pay attention! you maybe need to change the **"Endpoint" to your Server IP (Public Net) in the client file.**

$ awg show   # to checkout the status of AmneziaWG 
You can rerun this script to (add / remove/ Uninstall Services )the users 
$./amnezia-install.sh 

```
If you want to install AmneziaWG automatically you might be use below Application to configre your server.
* [AmneziaVPN Client](https://amnezia.org/downloads)
* [AmneziaWG Only (For iOS in AppStore)](https://github.com/amnezia-vpn/amneziawg-windows-client/releases)

# 使用步骤 (New)
终端执行： 
> python3 start_wireguard.py
*  选择 1 进行配置， 选择 2 重启 wireguard

# 使用步骤 (手动)


* step2 : chmod +x wireguard-install.sh
* step3 : sudo ./wireguard-install.sh
（注意开启默认的端口进站许可 UDP通讯协议）
* step4 : sudo vim /etc/sysctl.conf 
* step4 : net.ipv4.ip_forward=1
          net.ipv6.conf.all.forwarding=1
* step5 : sudo sysctl -p
* step6 : 设置开机自启：`sudo systemctl enable wg-quick@wg0`
* step7 : 激活wg0的接口：`sudo wg-quick up wg0`

* 如果在电脑端出现`ping www.google.com`通但无法上网 需要修改`xxx.conf`文件中的`MTU=1380`
