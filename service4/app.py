from application import app
from flask import Flask, Response, request

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)