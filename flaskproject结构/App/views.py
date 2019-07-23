import random

from flask import Blueprint, render_template, request, current_app, abort, jsonify
from sqlalchemy import and_

from App.extension import db, cache
from App.models import Student

blue = Blueprint('first_blue',__name__)


def init_blue(app):
    app.register_blueprint(blueprint=blue)


@blue.route('/')
def index():
    return 'Hello Flask'


@blue.route('/addstudent/')
def add_student():
    student = Student()
    student.name = '测试'
    student.age = random.randrange(100)
    db.session.add(student)
    db.session.commit()
    return '学生创建成功'


@blue.route('/getstudents/')
def get_students():
    students = Student.query.all()
    # students = Student.query.filter(Student.age.__gt__(50))  # 查询age>50的数据
    # students = Student.query.filter(Student.age>50)  # 查询age>50的数据
    # students = Student.query.order_by("age").all()  # 按照年龄排序,默认从小大到
    # students = Student.query.order_by(Student.age.desc())  # 按照年龄排序,从大到小
    # offset是跳过多少条，limit是输出多少条，如果order_by、limit、offset一起用，ordet_by必须放在最前面，其他两个顺序无所谓，但是都是先执行offset
    # students = Student.query.order_by("age").offset(10).limit(5)  # 按照年龄排序
    # students = Student.query.filter(Student.age>=10).filter(Student.age<80) # and的另一种用法，下面这个方法也可以
    students = Student.query.filter(and_(Student.age>=20,Student.age<70)) # and_、or_、not_的使用

    return render_template('get_students.html', students=students)


@blue.route('/modifystudent/')
def modify_student():
    student = Student.query.first()  # 查询出第一条
    student.name = '熊珍龙'
    db.session.add(student)
    db.session.commit()
    return '学生信息已经修改'


@blue.route('/deletestudent/')
def delete_student():
    student = Student.query.first()  # 查询出第一条
    db.session.delete(student)  # 删除记录
    db.session.commit()
    return '学生信息删除成功'


@blue.route('/fenye/')
def fenye():
    page = request.args.get("page",1,type=int)   # 从URL中获取页码，默认为1
    per_page = request.args.get("per_page",3,type=int)   # 从URL中获取每页显示显示的条数，默认3
    pagination = Student.query.paginate(page=page,per_page=per_page)  # 获取paginate对象
    # students = pagination.items  # 获取结果集,students就是一个列表

    return render_template('StudentList.html', pagination=pagination,per_page=per_page)


@blue.route('/config/')
@cache.cached(timeout=50, key_prefix='python')   # 使用装饰器实现缓存
def config():
    print('获取参数信息，这是应用了缓冲的效果')
    config = current_app.config
    for key in config:
        print(key,config.get(key))
    return render_template('config.html')


@blue.route('/cache/')  # 使用手动实现缓存
def get_cache():
    addr = request.remote_addr  # 获取访问的IP
    key = addr+'user'
    result = cache.get(key)
    # 判断，如果存在，则冲缓存中获取，如果不存在，则从数据库中获取
    if result:
        print(addr,'从缓存中加载数据')
        return result
    else:
        result = render_template('base.html')
        print(addr,'从数据库中加载数据，模拟')
        cache.set(key,result,timeout=30)
    return result


@blue.before_request  # 使用手动实现缓存，这个是钩子函数，注意区别，代表在所有访问之前被调用，常用于反扒
def before():
    print(request.remote_addr)
    print('before')

    # 通过useragent来进行反扒，useragent如果为空，则不允许访问,如requests.get不加请求头，则会报错。
    if not request.user_agent:
        abort(500)
    addr = request.remote_addr  # 获取访问的IP
    key = addr+'before'
    value = cache.get(key)
    # 判断，如果存在，则冲缓存中获取，如果不存在，则从数据库中获取
    if value:
        return '小伙子，别爬了'
    else:
        cache.set(key,'么么哒',timeout=30)


@blue.route('/score/')  # 前后端分析，通过json数据传递给前端静态网页，存在于static文件夹中
def get_score():
    score = {
        'data':[50,30,60,88,90]
    }
    return jsonify(score)
