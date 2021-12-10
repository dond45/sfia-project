from application import app
from flask import Flask, request, Response
import random

@app.route('/service4/prize', methods=['POST'])
def name():
    name = request.data.decode("utf-8")
    
    lst = string.split(',')
    name = lst[0]
    number = lst[1]

    if name == 'peter' and number == 1:
        prize = 'teddy'
    elif name == 'paul' and number == 2:
        prize = 'chocolate'
    elif name == 'john' and number == 3:
        prize = 'sweets'
    else:
        prize = "sorry! names and numbers did not match, you have won nothing! "
    return Response(prize, mimetype='text/plain')
