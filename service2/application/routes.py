from application import app
from flask import Flask, request, Response
import requests
import random

@app.route('/service2/name_gen', methods=['GET'])
def name_gen():
    name_gen = ["peter", "paul", "john"]
    name_gen = name[randint(0,2)]
    return Response(name, mimetype="text/plain")
    