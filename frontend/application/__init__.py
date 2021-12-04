from flask import Flask
# from application.models import prize_generator
from flask_sqlalchemy import SQLAlchemy

app = Flask (__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)

import application.routes