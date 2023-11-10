#!/usr/bin/env python3
from flask import Flask, session, request
from waitress import serve
import requests, threading, time

app = Flask(__name__)
app.config["SECRET_KEY"] = "c53ac69e07ed112ecb788eb4dc831990"

@app.route("/")
def main():
    session["auth"] = "True"
    session["username"] = "test" # SSTI may be applied with "{{ 3*7 }}"
    return "Check you cookies", 200

# Flask setup/start
thread = threading.Thread(target = lambda: serve(app, port=9000, host="127.0.0.1"))
thread.setDaemon(True)
thread.start()

# Request
time.sleep(1)
print(requests.get("http://localhost:9000/").cookies.get("session"))
