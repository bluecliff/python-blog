from werkzeug.security import generate_password_hash, check_password_hash
from blog import db
from sqlalchemy import desc
import datetime
from webhelpers.date import time_ago_in_words
from webhelpers.text import urlify

class Category(db.Model):
    __tablename__='category'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),unique=True)
    discription = db.Column(db.Text)

    def __unicode__(self):
        return self.name

class Person(db.Model):
    __tablename__ = 'person'
    id =db.Column(db.Integer,primary_key=True)
    lastname = db.Column(db.String(100))
    firstname = db.Column(db.String(100))
    email= db.Column(db.String(120),unique=True)
    pwdhash = db.Column(db.String(100))

    def __init__(self, firstname,lastname,email,password):
        self.firstname=firstname.title()
        self.lastname=lastname.title()
        self.email=email.lower()
        self.set_password(password)
    def __repr__(self):
        return '<User %r>' %(self.firstname)

    def set_password(self,password):
        self.pwdhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)

class Article(db.Model):
    __tablename__='articles'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text)
    created = db.Column(db.DateTime,default=datetime.datetime.utcnow)
    category_name = db.Column(db.String(10),db.ForeignKey(Category.name))
    category = db.relationship(Category)

    @classmethod
    def all(cls):
        return Article.query.order_by(desc(Article.created)).all()

    @classmethod
    def find_by_id(cls,id):
        return Article.query.filter(Article.id==id).first()

    @property
    def created_in_words(self):
        return time_ago_in_words(self.created)

    @property
    def slug(self):
        return urlify(self.title)


