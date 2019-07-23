# flask模型

Flask默认并没有提供任何数据库操作的API，我们可以选择任何适合自己项目的数据库来使用。python的ORM（SQLAlchemy）。针对于Flask的支持 pip install **flask-sqlalchemy**

数据连接格式： dialect+driver://username:password@host:port/database

- dialect数据库实现
- driver数据库的驱动
- username
- password
- host
- port
- database

## 1.Sqlite连接。

连接数据库需要指定配置

  app.config[‘SQLALCHEMY_DATABASE_URI’] = DB_URI

  app.config[‘SQLALCHEMY_TRAKE_MODIFICATIONS’]=False    禁止对象追踪修改

SQLite数据库连接不需要额外驱动，也不需要用户名和密码

SQLite连接的URI

  DB_URI = sqlite:///sqlite3.db

db = SQLAlchemy()

db.init_app(app)



**manager.py文件内容**：

```python
from flask import Flask
from flask_script import Manager
from App.views import blue
from App.models import init_db

app = Flask(__name__)
app.register_blueprint(blue)
manager = Manager(app=app)
# sqlite数据库配置，下面2条配置
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///sqlite3.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
init_db(app)  # 初始化db

if __name__ == '__main__':
    manager.run()
```

**models中的内容**：

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):   # 初始化db
    db.init_app(app)


class Person(db.Model):
    person_id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)  # 增加列
    person_name = db.Column(db.String(80), nullable=False)
```

**views中内容**：

```python
import random
from flask import Blueprint
from App.models import db, Person

blue = Blueprint('first_blue', __name__)  # __name__为导入的类名


@blue.route('/')
def index():
    return 'hello'


@blue.route('/createdb/')
def crate_db():
    db.create_all()
    return '数据库创建成功，这就是创建数据库的命令'


@blue.route('/createperson/')
def crate_person():
    person = Person()
    person.person_name = 'mark%d' % random.randrange(100)
    db.session.add(person)
    db.session.commit()
    return '人员创建成功，这就是插入数据的操作'

@blue.route('/get/')
def get():
    persons = Person.query.all()
    for person in persons:
        print(person.person_name)
    return '查询数据成功'
```

## 2.MySQL连接

```python
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:123456@localhost:3306/xzlmark'
```

只需要改变这个，其他不用修改。

更多用法请看：<https://flask-sqlalchemy.palletsprojects.com/en/2.x/>



# 3.SQLAlchemy其他知识

1.数据字段：

- 数字：**Integer**、SmallInteger  、BigInteger 、Float、**Numeric**

- 字符串：**String**、Text、Unicode、Unicode Text
- 时间：Date、Time、DateTime

2.常用约束

- primary_key
- autoincrement
- unique
- index
- nullable
- default
- ForeignKey()

3.数据操作

- db.create_all()   创建表
- db.drop_all()  删除表
- db.session.add(object)   插入单条数据
- db.session.addall(list[object])  插入列表数据
-  db.session.delete(object)  删除数据   是基于查询后进行的操作
-  db.session.commit()  事务提交，修改、增加、删除都需要提交事务。
- 修改和删除基于查询，需要先查询出来，然后再修改和删除。

4.数据查询

- 查询数据结果集，语法：  类名.query.xxx
- xxx可以是：**all()**  全部集、**first()** 第一条数据
- filter(类名.属性名.**运算符**(‘值’))   Student.query.filter(Student.age.__gt__(50))  # 查询age>50的数据
- filter(类名.属性 数学运算符  值)   Student.query.filter(Student.age>50)  # 查询age>50的数据,推荐使用这种方法

  常见的运算符：

- contains 
- startswith
- endswith
- in
- like
- __gt__   大于
- __ge__  大于等于
- __lt__  小于
- __le__  小于等于
- 与   and_   filter(and_(条件),条件…)
- 或    or_    filter(or_(条件),条件…)
- 非    not_    filter(not_(条件),条件…)

```python
students = Student.query.all()
    # students = Student.query.filter(Student.age.__gt__(50))  # 查询age>50的数据
    # students = Student.query.filter(Student.age>50)  # 查询age>50的数据
    # students = Student.query.order_by("age").all()  # 按照年龄排序,默认从小大到
    # students = Student.query.order_by(Student.age.desc())  # 按照年龄排序,从大到小
    # offset是跳过多少条，limit是输出多少条，如果order_by、limit、offset一起用，ordet_by必须放在最前面，其他两个顺序无所谓，但是都是先执行offset
    # students = Student.query.order_by("age").offset(10).limit(5)  # 按照年龄排序
    # students = Student.query.filter(Student.age>=10).filter(Student.age<80) # and的另一种用法，下面这个方法也可以
    students = Student.query.filter(and_(Student.age>=20,Student.age<70)) # and_、or_、not_的使用
```

5.数据分页paginate

使用关联的结果集：Student.query.paginate;每一页的数据量，所需的某一页的数据

方法和属性：

- pages  所有页数
- has_prev 是否有前一页
- prev_num  前一页的页数
- has_next 是否有下一页
- next_num 下一页的页数
- items 结果集
- ite_pages 可以迭代的页码对象

views中的实现

```python
@blue.route('/fenye/')
def fenye():
    page = request.args.get("page",1,type=int)   # 从URL中获取页码，默认为1
    per_page = request.args.get("per_page",3,type=int)   # 从URL中获取每页显示显示的条数，默认3
    pagination = Student.query.paginate(page=page,per_page=per_page)  # 获取paginate对象
    # students = pagination.items  # 获取结果集,students就是一个列表

    return render_template('StudentList.html', pagination=pagination,per_page=per_page)
```

模版文件中的实现：

```html
{% extends 'base.html' %}
{% block content %}
    <div class="container">
    <!--ul中的功能是实现数据的显示-->
        <ul>
            {% for student in pagination.items %}
                <li>{{ student.name}}</li>
            {% endfor %}
        </ul>
    <!--nav是bootstrap模版中的分页样式，可以从bootcss网站中找到-->
        <nav aria-label="Page navigation example">
            <ul class="pagination">
            <!--判断，如果前一页没有数据，则将前一页链接设置为不可用-->
                {% if pagination.has_prev %}
                    <li class="page-item"><a class="page-link"
                                             href="{{ url_for('first_blue.fenye') }}?page={{ pagination.prev_num }}&per_page={{ per_page }}">前一页</a>
                    </li>
                {% else %}
                    <li class="disabled"><a class="page-link" href="#">前一页</a></li>
                {% endif %}
                <!--迭代pages-->
                {%- for page in pagination.iter_pages() %}
                    {% if page %}
                        {% if page != pagination.page %}
                            <li class="page-item">
                                <a class="page-link"
                                   href="{{ url_for('first_blue.fenye') }}?page={{ page }}&per_page={{ per_page }}">{{ page }}</a>
                            </li>
                        {% else %}
                            <li class="active">
                                <a href="#" class="page-link">{{ page }}</a>
                            </li>
                        {% endif %}
                    {% else %}
                        <li class="page-item">
                            <a href="#" class="page-link">
                                <span class=ellipsis>…</span>
                            </a>
                        </li>

                    {% endif %}
                {%- endfor %}
<!--判断后一页是否还有数据-->
            {% if pagination.has_next %}
                    <li class="page-item"><a class="page-link"
                                             href="{{ url_for('first_blue.fenye') }}?page={{ pagination.next_num }}&per_page={{ per_page }}">Next</a>
                    </li>
                {% else %}
                    <li class="disabled"><a class="page-link" href="#">Next</a></li>
                {% endif %}
            </ul>
        </nav>
    </div>
{% endblock %}
```