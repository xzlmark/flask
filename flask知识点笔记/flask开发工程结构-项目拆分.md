# flask项目拆分

```
拆分主要目的是实现解耦合、使代码结构更清晰。
-manager 进行全局控制程序
    -init 初始化文件，初始化整个Flask对象、配置、路由、地三方库等
    -setting 配置项目所需的各种信息
    -views 用来处理业务逻辑，协调模版和模型
    -models 定义模型结构，获得数据库中的表的关系映射。
    -extension 项目的扩展库，第三方扩展库打包处理
    -extension 外部各种扩展
```

## manager.py

```python
from flask_migrate import MigrateCommand
from flask_script import Manager

from App import create_app

# 初始化app,通过懒加载的方式初始化
app = create_app()
manager = Manager(app=app)
# 把migrate和flask-script结合使用
manager.add_command('db', MigrateCommand)
if __name__ == '__main__':
    manager.run()
```



## __init__.py

```python
from flask import Flask
from App.extension import init_ext
from App.settings import envs
from App.views import init_blue


def create_app():
    # app初始化,并从配置文件中指定templates和static的地址
    app = Flask(__name__,template_folder=settings.TEMPLATE_FOLDER,static_folder=settings.STATIC_FOLDER)
    # 初始化配置,可以选择不同环境的配置
    app.config.from_object(envs.get('default'))
    # 注册蓝图、初始化蓝图
    init_blue(app)
    # 初始化第三方插件、库
    init_ext(app)
    return app
```



## setting.py

```python
# os.path.abspath(__file__) 返回的是文件的绝对路径：E:\python\project\flask学习\flaskproject结构\App\settings.py
# os.path.dirname(os.path.abspath(__file__)) 返回的是上一级目录E:\python\project\flask学习\flaskproject结构\App
# os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 返回的就是E:\python\project\flask学习\flaskproject结构
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 指定项目的地址
TEMPLATE_FOLDER = os.path.join(BASE_DIR, 'templates') # 指定templates文件夹的地址
STATIC_FOLDER = os.path.join(BASE_DIR, 'static') # 指定static文件夹的地址
def get_db_uri(dbinfo):
    ENGINE = dbinfo.get('ENGINE') or 'mysql'    # or后面是默认值
    DRIVER = dbinfo.get('DRIVER') or 'pymysql'
    USER = dbinfo.get('USER') or 'root'
    PASSWORD = dbinfo.get('PASSWORD') or '123456'
    HOST = dbinfo.get('HOST') or 'localhost'
    PORT = dbinfo.get('PORT') or '3306'
    NAME = dbinfo.get('NAME') or 'test'
    return f'{ENGINE}+{DRIVER}://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}'


class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = "123456789qwertyuiopasdfghjklzxcvbnm"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    DEBUG = True
    DATABASE = {
        'ENGINE':'mysql',
        'DRIVER':'pymysql',
        'USER':'root',
        'PASSWORD':'123456',
        'HOST':'localhost',
        'PORT':'3306',
        'NAME':'xzlmark'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class TestingConfig(Config):
    TESTING = True
    DATABASE = {
        'ENGINE':'mysql',
        'DRIVER':'pymysql',
        'USER':'root',
        'PASSWORD':'123456',
        'HOST':'127.0.0.1',
        'PORT':'3306',
        'NAME':'xzlmark_test'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class StagingConfig(Config):
    DATABASE = {
        'ENGINE':'mysql',
        'DRIVER':'pymysql',
        'USER':'root',
        'PASSWORD':'123456',
        'HOST':'127.0.0.1',
        'PORT':'3306',
        'NAME':'xzlmark_staging'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class ProductConfig(Config):
        DATABASE = {
            'ENGINE': 'mysql',
            'DRIVER': 'pymysql',
            'USER': 'root',
            'PASSWORD': '123456',
            'HOST': '127.0.0.1',
            'PORT': '3306',
            'NAME': 'xzlmark_product'
        }
        SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)

# 将不同的配置方案返回字典格式，方便在视图中调用
envs = {
    'develop':DevelopConfig,
    'testing':TestingConfig,
    'staging':StagingConfig,
    'product':ProductConfig，
    'default':DevelopConfig
}
```



## extension.py

```python
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# 创建sqlalchemy对象
db = SQLAlchemy()
# 创建Migrate数据库迁移对象
migrate = Migrate()


def init_ext(app):
    # 初始化db
    db.init_app(app=app)
    # 初始化migrate
    migrate.init_app(app=app, db=db)
```



## models.py

```python
from App.extension import db


# 这里使用的db是在extension中初始化后的对象,这里直接从extension中导入
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
```

## view.py

```python
from flask import Blueprint
from App.extension import db
from App.models import Student

blue = Blueprint('first_blue',__name__)


def init_blue(app): # 注册蓝图
    app.register_blueprint(blueprint=blue)


@blue.route('/')
def index():
    return 'Hello Flask'


@blue.route('/addstudent/')
def add_student():
    student = Student()
    student.name = '测试'
    db.session.add(student)
    db.session.commit()
    return '学生创建成功'

@blue.route('/getstudents/')
def get_students():
    students = Student.query.all()
    return render_template('get_students.html',students=students)
```



# 数据库迁移 flask-migrate

**Flask-Migrate** is an extension that handles SQLAlchemy database migrations for Flask applications using Alembic. The database operations are made available through the Flask command-line interface or through the Flask-Script extension.

这个插件的作用是：执行数据库迁移，在指定的数据库中（数据库必须先创建，不能创建数据库），根据models中的对象，自行创建相应的表。注意：在这个过程中，会将数据库先行清空，数据将不得保存，但是可以保存数据库结构，用升级和降级。

具体使用可以结合flask-script命令使用。

- 将数据模型映射到数据库

- 使用flask-migrate库

- 安装使用 pip install flask-migrate

- 初始化，需要使用app和数据库进行初始化：migrate = Migrate(app,db)

- 指令的使用：

  - python manager.py db init  初始化指令，仅可调用一次

  - migrate  生成迁移文件，内部迁移文件使用了链表来关联关系

  - upgrade 执行迁移文件，数据内容升级

    ​    --message 对迁移添加日志

  - downgrade 执行迁移文件，数据降级，相当于后悔药

  - --help 帮助文档

```python
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
```

# 拆分后路径的问题

按照上面拆分后，原有的结构被打破，app默认的根目录变为App的路径。如果这时按照原来的模版路径，则会提示找不到。这里有2中解决思路。

- ```
  app = Flask(__name__,template_folder='../templates')  # 在app初始化的时候指定路径，还可以指定static_folder
  ```

- 在配置文件中设置，然后在init初始化app的时候引进：

```
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_FOLDER = os.path.join(BASE_DIR, 'templates')
在init中设置：
app = Flask(__name__,template_folder=settings.TEMPLATE_FOLDER)
```

设置static的方法是一样的。