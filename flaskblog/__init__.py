from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy





app = Flask(__name__)
app.config['SECRET_KEY'] = '41e36ecef9ee47a506c491f073be7778'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes 