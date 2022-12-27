from flask import Flask
app = Flask(__name__)

@app.route('/paymnets')
def hello_world():
    return 'Hello, Docker!'
