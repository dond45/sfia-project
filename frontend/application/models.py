from flask import Flask, request, Response, render_template
import requests
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from application import routes
# from application import db

app = Flask (__name__)
db = SQLAlchemy(app)

class prize_generator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    number = db.Column(db.String(50), nullable=False)
    prize = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"{self.name}: { self.number}: {self.prize}"