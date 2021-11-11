from flask import request, redirect
from flask import session
from flask import render_template
from flask.helpers import url_for
from Servicios import ProductoService, DetallePedidoService, PedidoService, EstadoService
from Main import app

@app.route('/Pedido', methods = ['POST'])
def pedido():
    
    nombre_cliente = request.form["nombre_cliente"]
    apellido_cliente = request.form["apellido_cliente"]
    direccion_cliente = request.form["direccion_cliente"]
    departamento_cliente = request.form["departamento_cliente"]
    telefono_cliente = request.form["telefono_cliente"]
    detalles = session['carrito']
    
    session['carrito'] = []

    id_pedido = PedidoService.addPedido(nombre_cliente,
                                  apellido_cliente,
                                  direccion_cliente,
                                  departamento_cliente,
                                  telefono_cliente,
                                  detalles)
        
    return redirect(url_for('seguimiento',id_pedido=id_pedido))

#-----------------------------------------------------------
#                        SEGUIMIENTO 
#-----------------------------------------------------------
@app.route('/Pedido/<id_pedido>')
def seguimiento(id_pedido):   
    
    pedido = PedidoService.getPedidoById(id_pedido=id_pedido)
    
    if pedido is None:
        return render_template('pedido.html', pedidoExists=False) 
    else:
        estado = EstadoService.getEstadoById(pedido.id_estado)
        detallesPedido = DetallePedidoService.getDetallesPedidoByPedidoId(id_pedido=id_pedido)
        #Obtener productos del pedido
        productosVista = [] 
        total = 0
        for detallePedido in detallesPedido:
            producto = ProductoService.getProductoById(detallePedido.id_producto)
            cantidad = detallePedido.cantidad
            subtotal = producto.precio * cantidad
            total = total + subtotal
            productoVista = {"producto":producto,"cantidad":cantidad,"subtotal":subtotal}
            productosVista.append(productoVista)
                 
        return render_template('pedido.html', pedidoExists=True, pedido=pedido,productosVista=productosVista,estado=estado,total=total) 