from flask import Flask, request, redirect
from flask import session
from flask import render_template
from flask.helpers import url_for
from Modelos import Productos, DetallePedidos, Pedidos, Estados
from Modelos.DetallePedidos import DetallePedido

app = Flask(__name__, template_folder = 'Vistas',static_folder='Vistas')
app.secret_key = "SecretKey"


#------------------------------------------------------
#                       INDEX 
#------------------------------------------------------
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

#--------------------------------------------------------
#                       CARRITO
#--------------------------------------------------------
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


#--------------------------------------------------------
#                       PEDIDO 
#--------------------------------------------------------
@app.route('/Pedido', methods = ['POST'])
def pedido():
    
    nombre_cliente = request.form["nombre_cliente"]
    apellido_cliente = request.form["apellido_cliente"]
    direccion_cliente = request.form["direccion_cliente"]
    departamento_cliente = request.form["departamento_cliente"]
    telefono_cliente = request.form["telefono_cliente"]
    detalles = session['carrito']
    
    session['carrito'] = []

    id_pedido = Pedidos.addPedido(nombre_cliente,
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
    
    pedido = Pedidos.getPedidoById(id_pedido=id_pedido)
    
    if pedido is None:
        return render_template('pedido.html', pedidoExists=False) 
    else:
        estado = Estados.getEstadoById(pedido.id_estado)
        detallesPedido = DetallePedidos.getDetallesPedidoByPedidoId(id_pedido=id_pedido)
        #Obtener productos del pedido
        productosVista = [] 
        total = 0
        for detallePedido in detallesPedido:
            producto = Productos.getProductoById(detallePedido.id_producto)
            cantidad = detallePedido.cantidad
            subtotal = producto.precio * cantidad
            total = total + subtotal
            productoVista = {"producto":producto,"cantidad":cantidad,"subtotal":subtotal}
            productosVista.append(productoVista)
                 
        return render_template('pedido.html', pedidoExists=True, pedido=pedido,productosVista=productosVista,estado=estado,total=total) 
    
#------------------------------------------------------
#                       ALTA - BAJA 
#------------------------------------------------------

@app.route('/alta_baja', methods = ['GET','PUT','POST','DELETE'])
def altaBaja():
    productos = Productos.getAllProductos()
    return render_template('alta_baja.html', productos=productos)

#------------------------------------------------------
#                       LOGIN 
#------------------------------------------------------

@app.route('/login', methods = ['GET', 'POST'])
def login():
    
    return render_template('login.html')



#----------------------- RUN -----------------------

if __name__ == '__main__':
    app.run(debug=True,port=8000)

    
    
