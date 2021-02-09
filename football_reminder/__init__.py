from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
# sys.path.append("C:\\Users\\nima\\Desktop\\dev\\pyprojects\\football_reminder\\football_reminder")

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

from football_reminder import routes