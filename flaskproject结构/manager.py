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
