from flask import Flask
from flask_script import Manager
from APP.views import blue
from flask_session import Session
from flask_bootstrap import Bootstrap
app = Flask(__name__)

app.config['SECRET_KEY'] = '123456789wewjdfklsdjalsjdklasjdskadas'
app.config['SESSION_TYPE'] = 'redis'  # flask-session插件使用配置
Session(app=app) # flask-session插件使用配置
# bootatrap-flask 初始化
Bootstrap(app=app)
app.register_blueprint(blueprint=blue)

manager = Manager(app=app)


if __name__ == '__main__':
    manager.run()
