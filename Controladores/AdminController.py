from flask import request, redirect
from flask import session
from flask import render_template
from flask.helpers import url_for
from Servicios import ProductoService
from Main import app

@app.route('/admin', methods = ['GET','POST'])
def admin():
    #session['carrito'] = []
    return render_template('admin.html')
    
