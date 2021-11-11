from flask import render_template
from flask import request, redirect, url_for
from Servicios import ProductoService
from Main import app



@app.route('/admin/alta_baja')
def altaBaja():
    productos = ProductoService.getAllProductos()
    return render_template('alta_baja.html', productos=productos)



@app.route('/admin/modificacion', methods = ['POST'])
def modificacionReq():
    id_producto = request.form["id_producto"]
    return redirect(url_for('modificacion',id_producto=id_producto))



@app.route('/admin/modificacion/<id_producto>')
def modificacion(id_producto):
    producto = ProductoService.getProductoById(id_producto)
    return render_template('templates/productoForm.html', producto=producto, isUpdate=True)



@app.route('/admin/update', methods = ['POST'])
def productoUpdate():
    id_producto = request.form["id_producto"]
    producto = ProductoService.getProductoById(id_producto)
    producto.precio = float(request.form["precio"])
    producto.descuento = float(request.form["descuento"])
    producto.stock = int(request.form["stock"])
    producto.nombre_producto = request.form["nombre_producto"]
    producto.url_foto = request.form["url_foto"]
    ProductoService.updateProducto(producto)
    
    return redirect(url_for('altaBaja'))
     


@app.route('/admin/alta',methods = ['POST','GET'])
def alta(): 
    if request.method == 'POST':
        id_producto = ProductoService.addProducto(nombre_producto=request.form["nombre_producto"],
                                                  precio=float(request.form["precio"]),
                                                  descuento=float(request.form["descuento"]),
                                                  stock=int(request.form["stock"]),
                                                  url_foto=request.form["url_foto"])
        return redirect(url_for('altaBaja'))
    
    return render_template('templates/productoForm.html', isUpdate=False)



@app.route('/admin/baja',methods = ['POST'])
def baja():
    id_producto = request.form["id_producto"]
    ProductoService.deleteProductoById(id_producto)
    return redirect(url_for('altaBaja'))
