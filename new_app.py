from flask import Flask
from config import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello_world'

if __name__ == '__main__':
    app.run(host=HOST)