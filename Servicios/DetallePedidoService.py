from Modelos.Database.Restaurant import Restaurant 
from Modelos.DetallePedidos import DetallePedido

def getDetallesPedidoByPedidoId(id_pedido):
    session = Restaurant.getInstance().session
    detallesPedido = session.query(DetallePedido).filter_by(id_pedido=id_pedido)
    return detallesPedido

def addDetallePedido(id_producto,id_pedido,cantidad):
    session = Restaurant.getInstance().session    
    session.add(DetallePedido(id_producto=id_producto,id_pedido=id_pedido,cantidad=cantidad))
    session.commit()