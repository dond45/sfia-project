from application import app
from flask import Flask, request, Response
import requests
import random

@app.route('/service3/number_gen', methods=['GET'])
def number():
    Number = number[randint(0,2)]
    return Response(Number, mimetype="text/plain")