import uuid
from flask import Flask,render_template,url_for,request,make_response,redirect,abort,json
from flask import Response

from flask_script import Manager
app = Flask(__name__)

manager = Manager(app=app)
@app.route('/',methods=['GET','post'])
def hello_world():
    return 'Hello World!'


@app.route('/hello/')
def hello():
    return render_template('hello.html')


@app.route('/params/<name>')
def params(name):
    print(type(name))
    print(name)
    return '获取参数'


@app.route('/get/<path:name>')
def get(name):
    print(type(name))
    print(name)
    return '获取参数'


@app.route('/any/<any(a,b,c):an>')
def getuuid(an):
    print(type(an))
    print(an)
    return 'any'


@app.route('/url/')
def url():
    print(url_for('getuuid',an='a'))
    return '反向解析'


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

@app.route('/response/')
def res():
    response = make_response('<h1>这个是response对象</h1>',403)  # 注意，这里直接写第二个参数
    # response = Response('<h1>这个是response对象</h1>',status=403)
    return response


@app.route('/redirect/')
def red():
    res = redirect(url_for('hello'))
    return res


@app.route('/abort/')
def abor():
    abort(403)


@app.route('/json/')
def json_():
    # res = json.jsonify(name='xzl',age=31)
    result = '{"name":"xzl","age":31}'   # 如果直接传入，没问题，但是content-type还是text/html
    response = Response(response=result,content_type='application/json')
    return response


if __name__ == '__main__':
    manager.run()
