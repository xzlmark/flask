import os

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
    'product':ProductConfig,
    'default':DevelopConfig
}