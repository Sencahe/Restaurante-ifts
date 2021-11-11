from flask import Flask, request, redirect
from flask import session
from flask import render_template
from flask.helpers import url_for
from Modelos import Productos, DetallePedidos, Pedidos, Estados
from Modelos.DetallePedidos import DetallePedido
from Main import app

@app.route('/Carrito', methods = ['GET','PUT','POST','DELETE'])
def carrito():
    # Iniciar carrito
    if 'carrito' not in session:
        session['carrito'] = []
    # Eliminar o editar del carrito
    if request.method == 'POST':
        list = session["carrito"]
        carritoIndex = int(request.form["carritoIndex"])  
        
        if 'cantidad' not in request.form:   
            del list[carritoIndex]
            session['carrito'] = list
        else:
            carritoCantidad = int(request.form["cantidad"])
            list[carritoIndex]["cantidad"] = carritoCantidad
            
        session['carrito'] = list
        return redirect(url_for('carrito'))
    
    # Obtener Productos de Carrito
    productosVista = [] 
    for detalleCarrito in session["carrito"]:
        producto = Productos.getProductoById(detalleCarrito["id_producto"])
        cantidad= detalleCarrito["cantidad"]
        subtotal = cantidad * producto.precio
        productoVista = {"producto":producto,"cantidad":cantidad,"subtotal":subtotal}
        productosVista.append(productoVista)    
        
    return render_template('carrito.html', productosVista=productosVista)