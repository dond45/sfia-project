
from flask import Flask, request, Response
import requests
import random

from application import app

@app.route('/service2/name_gen', methods=['GET'])
def name_gen():
    names = ["peter", "paul", "john"]
    name_gen = names[randint(0,2)]
    return Response(name_gen[0], mimetype="text/plain")
    