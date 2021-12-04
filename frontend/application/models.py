from flask import Flask, request, Response, render_template
import requests
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from application import routes
from application import db

app = Flask (__name__)

class prize_generator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_gen = db.Column(db.String(25), nullable=False)
    number_gen = db.Column(db.String(50), nullable=False)
    prize_gen = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"{self.name_gen}: { self.number_gen}: {self.prize_gen}"

db.drop_all()
db.create_all()