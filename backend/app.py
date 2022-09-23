from flask import Flask,render_template
import json
from flask import Flask, request
from flask import jsonify

app = Flask(__name__, static_folder='static')

# API

@app.route('/')
def home(): 
    return jsonify({'data': 'Hello World!'})

@app.route('/twitter', methods=['GET', 'POST'])
def twitter():
    return 

if __name__ == '__main__':
    app.run(debug=True)
    
