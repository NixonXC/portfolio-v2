import flask
from flask import Flask, request, jsonify, render_template
import logging
import os
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data', methods=['GET'])
def get_data():
    app.logger.info('Data endpoint accessed')
    data = {"message": "This is some sample data"}
    return jsonify(data)

app.run(debug=True)