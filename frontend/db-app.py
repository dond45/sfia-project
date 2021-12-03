from flask import Flask, request, Response, render_template
import requests
from flask_sqlalchemy import SQLALchemy
from os import getenv


app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLALchemy(app)

class prize-generator():
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    prize = db.Column(db.String(50), nullable=False)
    car = db.Column(db.String, nullable=False)

db.drop_all()
db.create_all()