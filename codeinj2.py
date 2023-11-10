from flask import Flask, request
import os

# http://127.0.0.1:8080/search?filename=gatovsky.txt;ls -la
app = Flask(__name__)

@app.route('/search')
def search_files():
    filename = request.args.get('filename')
    command = "find / -name " + filename
    output = os.popen(command).read()
    return "Requested file is present at:" + output

if __name__ == '__main__':
    app.run(port=8080)