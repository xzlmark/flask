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


