from app import app, db 
from flask import render_template, request, redirect
import requests

# TODO: Render a form with input box
@app.route('/')
def index():
    return render_template('index.html')

# TODO: create a handler that checks whether user input is haiku or not
# TODO: handler should make a call to OpenAI API via Langchain
@app.route('/submit', methods=['POST'])
def submit():
    return render_template('result.html')