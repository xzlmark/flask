from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):   # 初始化db
    db.init_app(app)


class Person(db.Model):
    person_id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    person_name = db.Column(db.String(80), nullable=False)
