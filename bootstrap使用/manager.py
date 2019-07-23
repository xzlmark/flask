from flask import Flask
from flask_bootstrap import Bootstrap

from flask_script import Manager


from .App.views import blue

app = Flask(__name__)

Bootstrap(app=app)  # 实例化bootstrap


app.register_blueprint(blue)
manager = Manager(app=app)


if __name__ == '__main__':
    manager.run()