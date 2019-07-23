import random
from flask import Blueprint,render_template
from App.models import db, Person

blue = Blueprint('first_blue', __name__)  # __name__为导入的类名


@blue.route('/')
def index():
    return 'hello'


@blue.route('/createdb/')
def crate_db():
    db.create_all()
    return '数据库创建成功'


@blue.route('/createperson/')
def crate_person():
    person = Person()
    person.person_name = 'mark%d' % random.randrange(100)
    db.session.add(person)  # 插入数据的操作
    db.session.commit()  # 一定记得要提交
    return '人员创建成功'


@blue.route('/get/')
def get():
    persons = Person.query.all()

    return render_template('getList.html', persons=persons)
