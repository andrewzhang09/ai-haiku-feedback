from app import app, db 
from flask import render_template, request, redirect
import requests

from utils.submit_form_handler import form_handler

# TODO: Render a form with input box
# TODO: use tailwind css
@app.route('/')
def index():
    return render_template('index.html')

# TODO: save user inputs to SQLite database
@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form.get('user_input')
    return form_handler(user_input)