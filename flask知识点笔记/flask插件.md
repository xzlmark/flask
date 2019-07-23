# bootstrap-flask

是一个模版工具，可以对HTML进行美化。

```
1.安装：pip install bootstrap-flask
```

2.初始化：

```python
from flask_bootstrap import Bootstrap
from flask import Flask

app = Flask(__name__)

bootstrap = Bootstrap(app)
```

3.使用：

首先创建基础模版，其他HTML文件直接继承它即可，格式如下：

```html
<!doctype html>
<html lang="en">
  <head>
    {% block head %}
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    {% block styles %}
    <!-- Bootstrap CSS -->
    {{ bootstrap.load_css() }}
    {% endblock %}

    <title>基础模版文件</title>
    {% endblock %}
  </head>
  <body>
    <!-- Your page content -->
    {% block content %}{% endblock %}

    {% block scripts %}
    <!-- Optional JavaScript -->
    {{ bootstrap.load_js() }}
    {% endblock %}
  </body>
</html>
```

其中需要注意的是：

- <!doctype html>必须声明

- bootstrap-flask提供了两个函数来调用bootstrap，分别是放在head标签之间的{{ bootstrap.load_css() }}和放在body标签中的{{ bootstrap.load_js() }}

- <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"> 这个是必须要的。

# bootstrap-flask与bootstrap搭配使用

在前面已经定义了模版的基础上，在以后的文件中只需要继承即可使用bootstrap。如下面的child.html

```html
{% extends "base.html" %}

{% block content %}
<nav class="navbar navbar-expand-lg navbar-light bg-primary">
  <a class="navbar-brand" href="#">xzlmark</a>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="#">首页 <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">人民时评</a>
      </li>
        <li class="nav-item">
        <a class="nav-link" href="#">人民网</a>
      </li>
        <li class="nav-item">
        <a class="nav-link" href="#">半月谈</a>
      </li>
        <li class="nav-item">
        <a class="nav-link" href="#">知乎热榜</a>
      </li>
    </ul>
    </div>
</nav>
{% endblock %}
```

# Flask-DebugToolbar

这个是调试工具栏。

- 安装  pip install flask-debugtoolbar
- 使用  DebugToolbarExtension(app)
- 项目启动后，在浏览器中就可以看到调试工具栏

# flask-chache

运用缓存的主要作用是：提高访问效率，较少与数据库的交互；反扒

- 安装：pip install flask-cache
- 实例化 在ext中

```python
cache = Cache(config={
    'CACHE_TYPE':'redis',
    'CACHE_KEY_PREFIX':'python'
})
def init_ext(app):
    # 初始化db
    db.init_app(app=app)
    # 初始化缓存，flask-cache
    cache.init_app(app=app)
```

- 使用，有两种方式，一种是装饰器，一种是手动实现

## 提高访问效率

**装饰器用法：**

```python
@blue.route('/config/')
@cache.cached(timeout=50, key_prefix='python')   # 使用装饰器实现缓存
def config():
    print('获取参数信息，这是应用了缓冲的效果')
    config = current_app.config
    for key in config:
        print(key,config.get(key))
    return render_template('config.html')

```

**手动实现：**

```python
@blue.route('/cache/')  # 使用手动实现缓存
def get_cache():
    addr = request.remote_addr  # 获取访问的IP，根据IP来识别
    key = addr+'user'
    result = cache.get(key)
    # 判断，如果存在，则冲缓存中获取，如果不存在，则从数据库中获取
    if result:
        print(addr,'从缓存中加载数据')
        return result
    else:
        result = render_template('base.html')
        print(addr,'从数据库中加载数据，模拟')  
        cache.set(key,result,timeout=30)  # 第一次访问的时候就会将base.html缓存到result中
    return result

```

## **反扒实现（根据IP、useragent，同时结合钩子函数）**

```python
@blue.before_request  # 使用手动实现缓存，这个是钩子函数，注意区别，代表在所有访问之前被调用，常用于反扒
def before():
    print(request.remote_addr)
    print('before')

    # 通过useragent来进行反扒，useragent如果为空，则不允许访问,如requests.get不加请求头，则会报错。
    if not request.user_agent:
        abort(500)   # 抛出500错误
    addr = request.remote_addr  # 获取访问的IP
    key = addr+'before'
    value = cache.get(key)
    # 判断，如果存在，则冲缓存中获取，如果不存在，则从数据库中获取
    if value:
        return '小伙子，别爬了'
    else:
        cache.set(key,'么么哒',timeout=30)
```