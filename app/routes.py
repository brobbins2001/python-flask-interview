from flask import render_template, request, redirect, url_for
from app import app

@app.route('/')
def hello():
    # Candidate TODO: Render the hello_form.html template
    pass

@app.route('/submit', methods=['POST'])
def submit_name():
    # Candidate TODO: 
    # 1. Accept the POST data from the template.
    # 2. Render the display_name.html template with the posted data.
    pass