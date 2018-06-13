Mycat是一个开源的分布式数据库系统。中间件。可对接大部分数据库。用作分库分表分片。

[ubuntu 16.04 安装MyCat](https://www.cnblogs.com/piscesLoveCc/p/5764688.html)

# install JDK

去[官网](http://www.oracle.com/technetwork/java/javase/downloads/jdk10-downloads-4416644.html)下载SDK。

```sh
sudo mkdir /java
cd /home/cln/Downloads/
tar -zxvf jdk-10.0.1_linux-x64_bin.tar.gz
sudo mv jdk-10.0.1 /java/
sudo gedit /etc/environment
```
修改环境变量，内容如下：

```sh
export JAVA_HOME=/java/jdk-10.0.1
PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:$JAVA_HOME/bin"
export CLASSPATH=.:$JAVA_HOME/lib
```

```sh
source /etc/environment
java -version
```

# install mysql

详情查看[readme.md](https://github.com/CAOLINAN/PersonalNotes/blob/master/mysql/readme.md)

创建三个测试数据库

# install MyCat

[官方github](https://github.com/MyCATApache/Mycat-download)

[官方下载地址](http://dl.mycat.io/)

```sh
cd /home/cln/Downloads/
tar -zxvf Mycat-server-1.6-RELEASE-20161028204710-linux.tar.gz
sudo mv mycat/ /java/
sudo gedit /etc/environment
# 添加环境变量 /java/mycat/bin
source /etc/environment
mycat start
cd /java/mycat/conf

```
