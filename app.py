from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Kunj Acharya 12216328"
