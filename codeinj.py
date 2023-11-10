from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    name = request.values.get(name)
    cmd = 'nslookup ' + name

    return subprocess.Popen(cmd, shell=True)
    # return "Hello, {}!".format(name)


app.run()