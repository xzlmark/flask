# flask第一个简单程序

```python
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!!'
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')  
```

# flask第一插件：flask-script

功能：Flask Script扩展提供向Flask插入**外部脚本**的功能，包括运行一个开发用的服务器，一个定制的Python shell，设置数据库的脚本，cronjobs，及其他运行在web应用之外的命令行任务；使得脚本和系统分开。简言之就是通过命令行给run()传递参数，而不是直接向上面app.run()中直接设置参数。

用法：

pip install flask-script

初始化：使用app构建manager对象，Manager类追踪所有在命令行中调用的命令和处理过程的调用运行情况；

​                使用manager启动程序。Manager只有一个参数——Flask实例，也可以是一个函数或其他的返回Flask实例。调用manager.run()启动Manager实例接收命令行中的命令。

```python
from flask import Flask
from flask_script import Manager
app = Flask(__name__)

manager = Manager(app=app)
@app.route('/')
def hello_world():
    return 'Hello World!!'


if __name__ == '__main__':
    manager.run()
    
```

然后通过命令行工具，输入：

python manager.py **runserver** -d -p 8000 -h 127.0.0.1



runserver是启动服务器，可以指定参数，参数如下：

optional arguments:
  -?, --help            show this help message and exit
  -h HOST, --host HOST   主机
  -p PORT, --port PORT  端口
  --threaded
  --processes PROCESSES
  --passthrough-errors
  -d, --debug           enable the Werkzeug debugger (DO NOT use in production
                        code)   debug模式
  -D, --no-debug        disable the Werkzeug debugger
  -r, --reload          monitor Python files for changes (not 100% safe for
                        production use)   自动重新加载
  -R, --no-reload       do not monitor Python files for changes
  --ssl-crt SSL_CRT     Path to ssl certificate
  --ssl-key SSL_KEY     Path to ssl key



# flask的目录结构

static目录是存放静态资源的目录，如：css、script等；

templates目录是存放html文件的目录。html文件中引用css文件的格式为：<link rel="stylesheet" href="/static/css/hello_css.css">



# flask的请求流程

浏览器->route->views->（models）->views->templates->浏览器

# flask中参数

1.路径参数

​	位置参数

​	关键字参数

2.请求参数

​	get参数在路径中？之后

​	post参数在请求体

在flask中都是关键字参数，默认标识是尖括号<name>;

name需要和对应的视图函数的参数名字保持一致，参数允许有默认值。如果有默认值，那么在路由中，不传输参数也可以，如果没有默认值，参数在路由中必须传递。

```python
@app.route('/params/<name>')
def params(name):
    print(type(name))  # string类型
    print(name)
    return '获取参数'
```

默认参数类型是字符串，参数语法<<converter:var>> ,converter 是类型，还有int,float，path，UUID，any等

**path**:接收到的数据格式是字符串，特性会将斜线认为是一个字符。

```python
@app.route('/get/<path:name>')
def get(name):
    print(type(name))
    print(name)
    return '获取参数'
```

若在浏览器中输入：<http://127.0.0.1:8000/get/xzl/sds>

则会在终端输出：<class 'str'>  xzl/sds

**uuid**:约束，限制参数为UUID类型。import uuid      str(uuid.uuid4())  可以得到UUID

any:给定的任意一个,列出的元组中的任意一个。eg:

```python
@app.route('/any/<any(a,b,c):an>')
def getuuid(an):
    print(type(an))
    print(an)
    return 'any'
```

请求参数在flask中不是全部都支持的，是需要自己配置请求方法的，方法是在route中添加参数methods=['GET','POST']。

请求测试工具：postman、httpie

# flask反向解析

url_for：获取函数对应的路径。

```python
@app.route('/url/')
def url():
    print(url_for('getuuid',an='a'))
    return '反向解析'
```

输出结果为：/any/a

使用在app中，url_for('endpont') 即默认是函数的名字

在blueprint中，url_for('bluename.endpont'),蓝图名字.函数名

获取静态资源路径.url_for('static',filename='path')。static 资源，path相对于资源的相对路径

# flask请求-request

```python
@app.route('/request_test/',methods=['POST','GET'])
def request_test():
    print(request)
    # 请求的网址
    print(request.url)
    print(request.cookies)
    print(request.user_agent)
    # 请求的数据
    print(request.data)
    # 请求的表单数据
    print(request.form)
    # 请求的文件
    print(request.files)
    print(request.host)
    # get请求的参数
    print(request.args)
    # 请求方法
    print(request.method)
    return 'request'
```

如果需要获取参数的值，并且参数是字典格式的，那么可以用.get('key')来获取。

# flask中的response对象

视图函数返回接收两种类型

​	response对象

​	字符串：针对字符串会帮助我们包装成response对象

返回内容

​	1.返回的字符串

​	2.render_template.添加第二个参数，可以控制返回的状态码，数据正常，返回错误状态码

​	3.make_response():制作一个响应进行返回，参数是一个字符串或html内容，第二个参数是状态码

​	4.response:直接创建response进行返回，其实最终返回的都是response对象。

```python
@app.route('/response/')
def res():
    response = make_response('<h1>这个是response对象</h1>',403)  # 注意，这里直接写第二个参数
    # response = Response('<h1>这个是response对象</h1>',status=403)
    return response
```

# flask中的影响类型

response、redirect、abort、json

## flask中的redirect

```python
@app.route('/redirect/')
def red():
    res = redirect(url_for('hello'))
    return res
```

## flask中的abort

```python
@app.route('/abort/')
def abor():
    abort(403)
```

## flask中的json

返回json，使用jsonify将数据格式化为json格式，同时设置返回类型为application/json;

json.dumps将数据格式化为json格式，没有设置返回的数据类型，默认为text/html

```python
@app.route('/json/')
def json_():
    res = json.jsonify(name='xzl',age=31)   # 也可以直接将字典格式传入进去
    return res
```

还可以自己构造：

```python
@app.route('/json/')
def json_():
    # res = json.jsonify(name='xzl',age=31)
    result = '{"name":"xzl","age":31}'   # 如果直接传入，没问题，但是content-type还是text/html
    response = Response(response=result,content_type='application/json')  # 通过这种包装后，content-type就变为json了
    return response
```

# flask中蓝图的使用

Flask蓝图提供了模块化管理程序路由的功能，使程序结构清晰、简单易懂。

1.pip install flask-blueprint

2.使用蓝图：

```
from flask import Blueprint

blue = Blueprint('first_blue', __name__)   # __name__为导入的类名，蓝图名字不能重复
@blue.route('/')
def index():
   return '这是主页面'
```

3.在manager中注册蓝图：

```python
from flask import Flask
from flask_script import Manager
from flask学习.flask基础2.APP.views import blue

app = Flask(__name__)

app.register_blueprint(blueprint=blue)  # 需要在app中注册蓝图

manager = Manager(app=app)

if __name__ == '__main__':
    manager.run()
```

在蓝图中，url_for使用的是蓝图名.函数名。

# flask会话

## cookie

cookie是客户端会话技术，数据都死存在浏览器中，支持过期，不能跨域名、浏览器。flask中cookie是通过response来进行操作的。flask中的cookie可以直接支持中文，flask对cookie的内容作了编码

下面是简单的登录实验，使用的是cookie。

首先是home.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>home</title>
</head>
<body>
<h2>欢迎回来：{{username}}</h2>
<a href="{{url_for('first_blue.login',)}}">登录</a>
<a href="{{url_for('first_blue.logout',)}}">退出</a>
</body>
</html>
```

login.html

```html
<html>
<head>
   <meta charset="UTF-8">
    <title>login</title>
</head>
   <body>
      <form action = "{{url_for('first_blue.login')}}" method = "post">
         <p>Enter Name:</p>
         <p><input type = "text" name = "username" /></p>
         <p><input type = "submit" value = "submit" /></p>
      </form>

   </body>
</html>
```

对应的逻辑处理：

```python
@blue.route('/home/')
def home():
    name = request.cookies.get('name')  # 获取浏览器中的cookie，第一次请求是没有的
    return render_template('home.html',username=name)


@blue.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        # 构造response对象，设置cookie
        response = Response('登录成功%s' % username)
        response.set_cookie('name',username)
        return response



@blue.route('/logout/')
def logout():
    res = redirect(url_for('first_blue.home'))  #  重定向到home页
    res.delete_cookie('name')  # 删除cookie
    return res
```

## session

服务端会话技术，对数据进行数据安全操作，默认在内存中：不容易管理、容易丢失、不能多台电脑协作。

session导入的时候是实例化后的，不是Session.

```python
@blue.route('/home/')
def home():
    name = session.get('name')  # 获取浏览器中的session
    return render_template('home.html',username=name)


@blue.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
​        session['username'] = username   # 这里直接用即可
		  response = Response('登录成功%s' % username)

​        return response


@blue.route('/logout/')
def logout():
    res = redirect(url_for('first_blue.home')) 
    session['name']=''  # 删除cookie
    return res
```

除此之外，还需要在manager中设置：

```
app.config['SECRET_KEY'] = '123456789wewjdfklsdjalsjdklasjdskadas'
```

## flask-session

flask-session默认有效期为31天。

```python
from flask import Flask
from flask_script import Manager
from APP.views import blue
from flask_session import Session
app = Flask(__name__)

app.config['SESSION_TYPE'] = 'redis'  # flask-session插件使用配置
Session(app=app) # flask-session插件使用配置
app.register_blueprint(blueprint=blue)

manager = Manager(app=app)

if __name__ == '__main__':
    manager.run()
```

# flask中的4大内置对象

- request
- session
- config 一定要在程序初始化完成后调用
- g  可以使用它进行非正常数据传输，是全局的，如在before钩子函数中产生一个数据，需要在其他路由中使用，则可以用g进行获取，还可以在模版文件中使用。

config使用：

在HTML中获取全部的配置信息

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>config</title>
</head>
<body>
    {% for key in config %}
        <li>
        {{ key }}
        </li>
    {% endfor %}
</body>
</html>
```

在views中获取配置信息：

```python
@blue.route('/config/')
def config():
    config = current_app.config
    for key in config:
        print(key,config.get(key))
     print(config.get('DEBUG'))
    return render_template('config.html')
```

