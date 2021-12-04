from flask import Flask, Response, request, render_template
from flask_sqlalchemy import SQLAlchemy
import requests
# from application.models import prize_generator
from random import randint, random

from application import app

@app.route('/', methods=['GET'])
def home():
    name_gen = requests.get('http://service2:5000/service2/name_gen')
    number_gen = requests.get('http://service3:5000/service3/number_gen')
    prize_gen = requests.post('http://service4:5000/service4/prize_gen', data=prize_gen.text)
    prize_generator = Event(name_gen=name_gen.text, number_gen=number_gen.text, prize_gen=prize_gen.text)
    db.session.add(prize_generator)
    db.session.commit()
    eventor = Event.query.order_by(prize_generator.id.desc()).all()
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)