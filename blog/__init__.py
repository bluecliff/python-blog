from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:jsfli@localhost/mydatabase'

app.config.from_object('config')

db = SQLAlchemy()
db.app = app
db.init_app(app)

migrate = Migrate(app,db)
manager = Manager(app)

from blog import models
from blog import views