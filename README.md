---
author: Gray-Ice
---

该项目用于同步服务器和客户端的时间，精准度只有秒级，而且没有计算网络延迟。 写这些代码的目的只是为了在切换操作系统后V2ray能够正常运行(切换Windows到linux后系统时间可能会快或慢? 8个小时,这导致无法使用v2ray协议)。


## 安装依赖
其实要安装的只有supervisor,你完全可以用以下命令安装:
```shell
pip3 install supervisor
```
也可以sh install.sh

## 启动服务端程序
```shell
su
cd ./server
sh start_server.sh
```

## 客户端程序
以root身份运行以下命令即可与服务器同步时间:
```shell
python3 client.py
```
但每次都运行这条命令有点傻，还要切换到root，所以我建议在sudoers里给当前用户加上date的免root使用权限，然后就可以直接把这条命令加到.bashrc或.zshrc里了。
sudoers配置如下:
```config
yourusername ALL=(ALL) NOPASSWD: /your/path/date
```
