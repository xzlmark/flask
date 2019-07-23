from flask import Blueprint,render_template
blue = Blueprint('first_blue', __name__)  # __name__为导入的类名


@blue.route('/')
def index():
    return render_template('base.html')


@blue.route('/base/')
def base():
    return render_template('child.html')


@blue.route('/index/')
def shouye():
    return '首页'