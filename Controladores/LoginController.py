from flask import Flask, request, redirect
from flask import session
from flask import render_template
from flask.helpers import url_for
from Modelos import Productos, DetallePedidos, Pedidos, Estados
from Modelos.DetallePedidos import DetallePedido
from Main import app

@app.route('/login', methods = ['GET', 'POST'])
def login():
    
    return render_template('login.html')


