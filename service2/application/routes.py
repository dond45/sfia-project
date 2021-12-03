from application import app
from flask import Flask, request, Response
import requests
import random

@app.route('/service2/name', methods=['GET'])
def name():
    name = ["peter", "paul", "john"]
    Name = name[randint(0,2)]
    return Response(Name, mimetype="text/plain")
    