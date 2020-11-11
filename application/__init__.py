from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:password1234@35.197.211.81/todo" 
app.config['SECRET_KEY'] = "the-secret"

db = SQLAlchemy(app)


from application import routes
