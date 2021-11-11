from datetime import datetime
from Modelos.Database.Restaurant import Restaurant
from Modelos.Pedidos import Pedido
from Servicios import DetallePedidoService

def getPedidoById(id_pedido):
    session = Restaurant.getInstance().session
    try:
        pedido = session.query(Pedido).filter_by(id_pedido = id_pedido).one()
        return pedido
    except Exception as e:
        print(e)
        return None
    
    
 
def addPedido(nombre_cliente,apellido_cliente,direccion_cliente,departamento_cliente,telefono_cliente,detalles):
    
    session = Restaurant.getInstance().session
    
    pedido = Pedido(nombre_cliente=nombre_cliente,
                    apellido_cliente=apellido_cliente,
                    direccion_cliente=direccion_cliente,
                    departamento_cliente=departamento_cliente,
                    telefono_cliente=telefono_cliente,
                    id_estado=1,
                    fecha_pedido=datetime.now())
    
    session.add(pedido)
    session.flush()
    
    for detalle in detalles:
        DetallePedidoService.addDetallePedido(id_pedido=pedido.id_pedido,
                                        id_producto=detalle["id_producto"],
                                        cantidad=detalle["cantidad"])
    
    session.close()
    return pedido.id_pedido