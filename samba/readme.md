# 建立文件仓库
## 在一台服务器安装samba
[链接教程](http://blog.topspeedsnail.com/archives/7511)
```bash
sudo apt-get install samba samba-common
sudo systemctl stop ufw
mkdir ipfs
sudo vim /etc/samba/smb.conf
```
```vim
[ipfs]
    comment = Ipfs Directories
    browseable = no
    path = /home/ubuntu/ipfs
    valid users = ubuntu
    read only = no
```
```bash
sudo smbpasswd -a ubuntu
```
password:123
## 在其他ubuntu服务器安装samba客户端
[链接教程](https://blog.csdn.net/zcf1002797280/article/details/49805603)
```bash
sudo apt-get install smbclient
smbclient -L 10.175.0.97
sudo apt install cifs-utils
mkdir ipfs
mount -t cifs -o username=ubuntu,password=123 //10.175.0.97/ipfs /home/ubuntu/ipfs
```
## 在其他windows服务器
直接在文件夹地址栏访问<b>\\\10.175.0.97\ipfs</b>输入用户名ubuntu和密码123

# Centos7
Centos7 的配置文件和前几系列有所不同。请注意……