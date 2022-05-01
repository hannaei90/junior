
from flask import Flask, request, render_template, jsonify
from junior_model import store_in_dictionary, load, save_dictionary, clear_dictionary
from junior_model import dictionary, get_dictionary

app = Flask(__name__)

@app.route('/')
def home():
    load()
    return render_template('form.html')

@app.route('/add', methods=['GET'])
def add():
    key = request.args['key']
    value = request.args['value']
    store_in_dictionary(key,value)
    save_dictionary()
    return render_template('form.html')

@app.route('/print')
def print():
    return render_template('table.html', dictionary=get_dictionary())

@app.route('/clear', methods=['GET'])
def clear():
    clear_dictionary()
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True,  port=8080)
