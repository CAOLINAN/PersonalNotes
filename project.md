# 技术路线引用自知乎，随时更改
## python
SocketServer 。补上socket模块知识，熟悉TCP/UDP编程，了解Mixin机制的最佳例SocketServer.{ForkingMixIn|ThreadingMixIn}
了解thread/threading 模块，了解并发，读取select模块，对epoll/kqueue深刻理解，学习异步框架asyncore和asynchat
以TCP/UDP协议为基础的应用读gevent和greenlet
web端则读BaseHTTPServer、SimpleHTTPServer和CGIHTTPServer，读cgi/cgitb,自己随意写框架，读cookielib，读wsgiref，写一个简单的web framework
酌情选择flask、web.py、DJango、pyramid，学习httplib/urllib/urlpase