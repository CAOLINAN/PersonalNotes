# 说明
thrift为Facebook开发，需要用IDL定义通用的服务接口，并通过生成不同的语言代理实现来达到跨语言、平台的功能。
在其中可以定义基本数据类型、结构体、容器、异常、服务。

命令 thrift -r --gen py tutorial.thrift