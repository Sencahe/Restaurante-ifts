from flask import Flask, request, redirect
from flask import session
from flask import render_template
from flask.helpers import url_for
from Modelos import Productos, DetallePedidos, Pedidos, Estados
from Modelos.DetallePedidos import DetallePedido
from Main import app

@app.route('/', methods = ['GET','POST'])
def index():
    # Iniciar carrito
    if 'carrito' not in session:
        session['carrito'] = []
    
    # Agregar a carrito
    if request.method == 'POST':
        id_producto = int(request.form["id_producto"])
        cantidad = int(request.form["cantidad"])
        list = session["carrito"]
        list.append({"id_producto":id_producto,"cantidad":cantidad})
        session['carrito'] = list  
        return redirect(url_for('index'))
    
    # Obtener Productos
    productos = Productos.getAllProductos()
    productosVista = []
    for producto in productos:
        productoVista = {"producto":producto,"cantidad":1,"subtotal":producto.precio}
        productosVista.append(productoVista)
    
    return render_template('index.html', productosVista=productosVista)
