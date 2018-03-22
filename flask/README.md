**flask**

*[英文文档](http://flask.pocoo.org/docs/0.12/)*

*[中文文档](http://docs.jinkan.org/docs/flask/)*

*[源码](https://github.com/pallets/flask/)*

# 安装
pip install Flask

## Werkzeug
德语 工具
是一个WSGI的工具集

## Jinja2
日语 神社
负责渲染模板

# Flask类
实例为WSGI应用程序

## run
可接受参数
> host

> port

> debug

# 路由
## 装饰器添加路由 
```python
@app.route('/')
def index():
    return 'Index Page'
```
index函数绑定到根访问路径下

## 装饰器添加路由变量
```python
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username
```
地址中user后面将用户名传入到方法中调用。

>tip:可以标明参数类型。目前支持三种:int, float, path
```python
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
```

## 唯一URL
```python
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
```
第一条可以通过URL“/project”或者“/project/”均可访问
第二种只能通过URL“/about”访问

## 构造URL
url_for()根据方法反向返回URL请求。参数为方法名，也可以接受URL规则的变量部分来命名参数。

>tip:url_for()需要用到 test_request_context()的环境。

示例如下：
```python
>>> from flask import Flask, url_for
>>> app = Flask(__name__)
>>> @app.route('/')
... def index(): pass
...
>>> @app.route('/login')
... def login(): pass
...
>>> @app.route('/user/<username>')
... def profile(username): pass
...
>>> with app.test_request_context():
...  print url_for('index')
...  print url_for('login')
...  print url_for('login', next='/')
...  print url_for('profile', username='John Doe')
...
/
/login
/login?next=/
/user/John%20Doe
```

## HTTP方法
HTTP 方法如下表：
HTTP版本|方法(原始)|方法(新增)
-|-|
1.0||GET、POST、HEAD
1.1|GET、POST、HEAD|OPTIONS、PUT、DELETE、TRACE、CONNECT

方法描述如下表：
方法|描述
-- | -------------
GET|请求指定的页面信息，并返回实体主体
POST|向指定资源提交数据进行处理请求。可能导致新的资源建立或已有资源修改
HEAD|类似GET请求，获取报头
PUT|从客户端向服务端传送的数据取代指定文档的内容
DELETE|删除指定页面
CONNECT|预留给可以将连接改为管道方式的代理服务器
OPTIONS|允许客户端查看服务器性能
TRACE|回显服务器收到的请求，主要用于测试或诊断

flask处理HTTP方法示例如下:
```bash
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()
```

方法|描述
-|:-
GET|flask默认添加HEAD，遵循HTTP RFC
POST|HTML表单通常发送数据到服务器的方法，通知服务器确保数据存储且仅存一次
HEAD|无需人工处理，底层Werkzeug实现辅助功能
PUT|类似POST，但触发多次存储过程，多次会覆盖旧值
DELETE|删除指定页面
OPTIONS|0.6之后实现自动处理，让客户端可以知道支持的方法
TRACE|回显服务器收到的请求，主要用于测试或诊断