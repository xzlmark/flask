from App.extension import db


# 这里使用的db是在extension中初始化后的对象
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)


class Person(db.Model):
    id = db.Column(db.INTEGER,primary_key=True,autoincrement=True)
    name = db.Column(db.String(20))


class Animal(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))