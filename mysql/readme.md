# mysql 安装

```sh
sudo apt update
sudo apt install mysql-server mysql-client libmysqlclient-dev
```

# mysql 配置

[mysql配置文件](http://www.cnblogs.com/EasonJim/p/7158466.html)


# [mysql 设置远程连接用户登录](https://www.cnblogs.com/lonlywaiting/p/6307702.html)

```sh
# 登录mysql
mysql -h 192.168.14.45 -P 3306 -u root -p
# 输入123
```

```sh
# 创建用户名为user，密码为123的远程访问用户
grant all on *.* to user@'%' identified by '123'; # look warning when error
flush privileges;
# 查询是否添加user用户成功
use mysql
select user,host,authentication_string from user;
quit
sudo systemctl restart mysql
```

> warning：出现ERROR 1819 (HY000): Your password does not satisfy the current policy requirements

[解决方式](https://www.cnblogs.com/ivictor/p/5142809.html)

```sh
set global validate_password_policy=0;
SHOW VARIABLES LIKE 'validate_password%';
set global validate_password_length=1;
set global validate_password_mixed_case_count=1;

```

自动化创建数据库脚本（未测试）

```sh
# 创建脚本
db_host=( "192.168.1.21" "192.168.1.22" "192.168.1.22" )
db_port=( "3307" "3307" "3308" )
mysql_user=root
mysql_passwd=root123
mysql_cmd="/application/mysql/bin/mysql -u$mysql_user -p$mysql_passwd -e"
for (( i=0;i<${#db_host[@]};i++ )) 
do
        db="-h${db_host[$i]} -P${db_port[$i]}";
        for (( j=1;j<=4;j++ ))
        do
                n=$(( $i*4+$j ))
                [ $n -lt 10 ] && db_name="message20160"$n || db_name="message2016"$n
                $mysql_cmd "drop database if exists $db_name" $db >/dev/null 2>&1
                echo "creating database "$db_name"..."
                $mysql_cmd "create database $db_name;" $db >/dev/null 2>&1
 
                $mysql_cmd "use $db_name;source /data/tb.sql;" $db 2>/dev/null
        done
 
        $mysql_cmd "show databases;" $db 2> /dev/null
done
```
