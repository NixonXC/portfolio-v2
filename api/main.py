import os
import sys
import logging
import flask
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    print("Critical Error: Missing SUPABASE_URL or SUPABASE_KEY environment variables.")
    sys.exit(1)

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data', methods=['GET'])
def get_data():
    app.logger.info('Data endpoint accessed')
    data = {"message": "This is some sample data"}
    return jsonify(data)

@app.route('/api/contact', methods=['POST'])
def submit_contact():
    app.logger.info('Contact form submission received')
    
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form

    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    if not name or not email or not message:
        return jsonify({"success": False, "error": "All fields (name, email, message) are required."}), 400

    try:
        payload = {
            "name": name,
            "email": email,
            "message": message
        }
        
        response = supabase.table("contact_submissions").insert(payload).execute()
        
        if not response.data:
            return jsonify({"success": False, "error": "Failed to log entry into the database repository."}), 400
            
        return render_template('success.html', success=True, name=name, status="Successfully", message="Your message has been successfully submitted. We will get back to you shortly.")
    except Exception as e:
        app.logger.error(f"Supabase handling error occurred: {str(e)}")
        return render_template('success.html', success=False, name=name, status="Failed", message="There was an error submitting your message. Please try again later."), 500

if __name__ == '__main__':
    app.run()
