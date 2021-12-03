from flask import Flask, Response, request
import requests
from random import randint

from application import app

@app.route('/', methods=['GET'])
def name():
    name = requests.get('http://service2:5000/service2/name')
    prize = requests.get('http://service3:5000/service3/number')
    
    car = requests.post('http://service4:5000/service4/prize', data=prize.text)
    
    return render_template('index.html', name=name.text, prize=prize.text, car=car.text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)