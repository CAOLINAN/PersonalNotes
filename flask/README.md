**flask**

*[Ӣ���ĵ�](http://flask.pocoo.org/docs/0.12/)*

*[�����ĵ�](http://docs.jinkan.org/docs/flask/)*

*[Դ��](https://github.com/pallets/flask/)*

# ��װ
pip install Flask

## Werkzeug
���� ����
��һ��WSGI�Ĺ��߼�

## Jinja2
���� ����
������Ⱦģ��

# Flask��
ʵ��ΪWSGIӦ�ó���

## run
�ɽ��ܲ���
> host

> port

> debug

# ·��
## װ�������·�� 
```python
@app.route('/')
def index():
    return 'Index Page'
```
index�����󶨵�������·����

## װ�������·�ɱ���
```python
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username
```
��ַ��user���潫�û������뵽�����е��á�

>tip:���Ա����������͡�Ŀǰ֧������:int, float, path
```python
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
```

## ΨһURL
```python
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
```
��һ������ͨ��URL��/project�����ߡ�/project/�����ɷ���
�ڶ���ֻ��ͨ��URL��/about������

## ����URL
url_for()���ݷ������򷵻�URL���󡣲���Ϊ��������Ҳ���Խ���URL����ı�������������������

>tip:url_for()��Ҫ�õ� test_request_context()�Ļ�����

ʾ�����£�
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

## HTTP����
HTTP �������±�
HTTP�汾|����(ԭʼ)|����(����)
-|-|
1.0||GET��POST��HEAD
1.1|GET��POST��HEAD|OPTIONS��PUT��DELETE��TRACE��CONNECT

�����������±�
����|����
-- | -------------
GET|����ָ����ҳ����Ϣ��������ʵ������
POST|��ָ����Դ�ύ���ݽ��д������󡣿��ܵ����µ���Դ������������Դ�޸�
HEAD|����GET���󣬻�ȡ��ͷ
PUT|�ӿͻ��������˴��͵�����ȡ��ָ���ĵ�������
DELETE|ɾ��ָ��ҳ��
CONNECT|Ԥ�������Խ����Ӹ�Ϊ�ܵ���ʽ�Ĵ��������
OPTIONS|����ͻ��˲鿴����������
TRACE|���Է������յ���������Ҫ���ڲ��Ի����

flask����HTTP����ʾ������:
```bash
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()
```

����|����
-|:-
GET|flaskĬ�����HEAD����ѭHTTP RFC
POST|HTML��ͨ���������ݵ��������ķ�����֪ͨ������ȷ�����ݴ洢�ҽ���һ��
HEAD|�����˹������ײ�Werkzeugʵ�ָ�������
PUT|����POST����������δ洢���̣���λḲ�Ǿ�ֵ
DELETE|ɾ��ָ��ҳ��
OPTIONS|0.6֮��ʵ���Զ������ÿͻ��˿���֪��֧�ֵķ���
TRACE|���Է������յ���������Ҫ���ڲ��Ի����