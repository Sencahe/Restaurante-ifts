from flask import Flask, request, redirect
from flask import session
from flask import render_template
from flask.helpers import url_for
from Modelos import Productos, DetallePedidos, Pedidos, Estados
from Modelos.DetallePedidos import DetallePedido
from Main import app

@app.route('/alta_baja', methods = ['GET','PUT','POST','DELETE'])
def altaBaja():
    productos = Productos.getAllProductos()
    return render_template('alta_baja.html', productos=productos)