import flask
from flask import Flask, request, jsonify, render_template
import os
import sys

app = Flask(__name__)
# Configure logging
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {"message": "This is some sample data"}
    return jsonify(data)

app.run()
