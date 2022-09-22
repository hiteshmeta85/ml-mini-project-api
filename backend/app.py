from flask import Flask,render_template
import json
from flask import Flask, request


app = Flask(__name__, static_folder='static')


@app.route('/')
def home(): 
    return render_template('home_page.html')

@app.route('/twitter', methods=['GET', 'POST'])
def twitter():
    return 


if __name__ == '__main__':
    app.run(debug=False)
    
