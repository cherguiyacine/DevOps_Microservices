# save this as app.py
from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello():
    print("Welcome to server")
    name = request.args.get("name", "World")
    return 'Hello to the server, {escape(name)}!'