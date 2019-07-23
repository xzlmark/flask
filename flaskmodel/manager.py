from flask import Flask
from flask_script import Manager
from App.views import blue
from App.models import init_db

app = Flask(__name__)
app.register_blueprint(blue)
manager = Manager(app=app)

# sqlite数据库配置，下面3条配置
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///sqlite3.db'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:123456@localhost:3306/xzlmark'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
init_db(app)  # 初始化db


if __name__ == '__main__':
    manager.run()

