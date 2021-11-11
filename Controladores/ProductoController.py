from flask import render_template
from Servicios import ProductoService
from Main import app

@app.route('/alta_baja', methods = ['GET','PUT','POST','DELETE'])
def altaBaja():
    productos = ProductoService.getAllProductos()
    return render_template('alta_baja.html', productos=productos)