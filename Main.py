from flask import Flask, request, redirect
from flask import session
from flask import render_template
from flask.helpers import url_for
from Modelos import Productos, DetallePedidos, Pedidos, Estados
from Modelos.DetallePedidos import DetallePedido

app = Flask(__name__, template_folder = 'Vistas',static_folder='Vistas')
app.secret_key = "SecretKey"

@app.route('/', methods = ['GET','POST'])
def index():
    # Iniciar carrito
    if 'carrito' not in session:
        session['carrito'] = []
    # Obtener Productos
    productos = Productos.getAllProductos()
    # Agregar a carrito
    if request.method == 'POST':
        id_producto = int(request.form["id_producto"])
        cantidad = int(request.form["cantidad"])
        list = session["carrito"]
        list.append({"id_producto":id_producto,"cantidad":cantidad})
        session['carrito'] = list  
        return redirect(url_for('index'))
    
    return render_template('index.html', productos=productos)


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
    productos = [] 
    for productoCarrito in session["carrito"]:
        producto = Productos.getProductoById(productoCarrito["id_producto"])
        producto.cantidad = productoCarrito["cantidad"]
        productos.append(producto)    
        
    return render_template('carrito.html', productos=productos)


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


@app.route('/Pedido/<id_pedido>')
def seguimiento(id_pedido):   
    
    pedido = Pedidos.getPedidoById(id_pedido=id_pedido)
    
    if pedido is None:
        return render_template('pedido.html', pedidoExists=False) 
    else:
        estado = Estados.getEstadoById(pedido.id_estado)
        detallesPedido = DetallePedidos.getDetallesPedidoByPedidoId(id_pedido=id_pedido)
        productos = [] 
        total = 0
        for detallePedido in detallesPedido:
            producto = Productos.getProductoById(detallePedido.id_producto)
            producto.cantidad = detallePedido.cantidad
            productos.append(producto)
            total = total + producto.precio * producto.cantidad
        
        return render_template('pedido.html', pedidoExists=True, pedido=pedido,productos=productos,estado=estado,total=total) 
    


#------------- RUN -----------------------
if __name__ == '__main__':
    app.run(debug=True,port=8000)

    
    
