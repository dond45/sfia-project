from flask import Flask, Response, request
import requests

from application import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)