from flask import Blueprint, render_template,request,Response,redirect,url_for,session

blue = Blueprint('first_blue', __name__)  # __name__为导入的类名


@blue.route('/')
def index():
    return render_template('index.html')


'''
PyQuery 的用法@blue.route('/douyin/')
def douyin():
    doc = pq(text)
    text = str(doc('.l_container'))
    return text
'''


@blue.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        session['name'] = username
        response = Response('登录成功%s' % username)
        # response.set_cookie('name',username)
        return response


@blue.route('/home/')
def home():
    # name = request.cookies.get('name')
    name = session.get('name')
    return render_template('home.html',username=name)


@blue.route('/logout/')
def logout():
    res = redirect(url_for('first_blue.home'))
    session['name']=''
    return res


@blue.route('/bootstrap/')
def bootstrap():
    return render_template('boot.html')