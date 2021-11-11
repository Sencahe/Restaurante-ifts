from flask import request, redirect
from flask import session
from flask import render_template
from flask.helpers import url_for
from Main import app

@app.route('/login', methods = ['GET', 'POST'])
def login():
    
    return render_template('login.html')


