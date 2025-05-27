import flask
from flask import Flask, request, jsonify, render_template
import logging
import os
import sys
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
# Configure logging
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
app.logger.addHandler(handler)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data', methods=['GET'])
def get_data():
    app.logger.info('Data endpoint accessed')
    data = {"message": "This is some sample data"}
    return jsonify(data)

app.run(debug=True)