# 常用sql语句

mysql -uuser -p123456 -h127.0.0.1 -P3306 -Dallblockinfo_development

mysql -uuser -p123456 -h127.0.0.1 -P8066 -Dallblockinfo_development

select count(*) from block;

# 性能优化

mycat性能优化参考网址 https://blog.csdn.net/tornadojava/article/details/54948662

mycat主从同步 https://blog.csdn.net/mchdba/article/details/50616534

mysql性能优化参考网址 http://tsaikoga.github.io/blog/2018/05/12/mysql-xing-neng-you-hua/#2.4

mysql详细介绍 https://tech.meituan.com/mysql-index.html

# 慢查询

在设置中开启sql慢查询

# docker启动

docker pull mysql

```sh
$ docker run --name some-mysql \
			-v /my/custom:/etc/mysql/conf.d \
			-v /my/own/datadir:/var/lib/mysql \
			-e MYSQL_ROOT_PASSWORD=my-secret-pw \
			-d mysql:tag \
			--character-set-server=utf8mb4 \
			--collation-server=utf8mb4_unicode_ci

name:some-mysql为容器名，

/my/custom/config-file.cnf为数据库配置文件

/my/own/datadir 为数据目录

my-secret-pw为root密码，

mysql:tag为mysql镜像版本。 

character-set-server为mysql字符集

collation-server
```

其他参数信息可以查阅帮助

```sh
docker run -it --rm mysql:tag --verbose --help
```


docker run --name mysql01 -v /home/mysqlconf:/etc/mysql/conf.d -v /home/mysql01/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=12345678 -p 3306:3306 -d mysql --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci


docker run --name mysql01 \
	-v /home/mysqlconf:/etc/mysql/conf.d \
	-v /home/mysql01/data:/var/lib/mysql \
	-v /home/mysql01/log:/var/log \
	-e MYSQL_ROOT_PASSWORD=12345678 \
	-p 3306:3306 \
	-d mysql:5.7.22 \
	--character-set-server=utf8mb4 \
	--collation-server=utf8mb4_unicode_ci
