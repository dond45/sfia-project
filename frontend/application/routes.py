from flask import Flask, Response, request, render_template
from flask_sqlalchemy import SQLAlchemy
import requests
# from application.models import prize_generator
from random import random

from application import app

from application import db

@app.route('/', methods=['GET'])
def home():
    name_gen = requests.get('http://service2-api:5000/service2/name_gen')
    number_gen = requests.get('http://service3-api:5000/service3/number_gen')
    prize_gen = requests.post('http://service4-api:5000', data=name_gen.text+','+number_gen.text)
    

    # last_five_prizes = prize_generator.query.all()
    # db.session.add(
    #     prize_generator(
    #         name = name.text,
    #         number = number.text,
    #         prize = prize.text 
    #     )
    # )
    # db.session.commit()

    # eventor = Event.query.order_by(prize_generator.id.desc()).all()

    return render_template('index.html', name_gen1=name_gen.text, number_gen1=number_gen.text, prize_gen1=prize_gen.text, last_five_prizes=last_five_prizes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)