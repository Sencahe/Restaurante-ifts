from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from Modelos.Database.Restaurant import Restaurant 
from Modelos import DetallePedidos, Estados, Administradores, Repartidores

#----------- DAO -----------------
Base = declarative_base()

class Pedido(Base):
    
    __tablename__ = 'Pedidos'
    
    id_pedido =  Column(Integer(),primary_key=True,autoincrement=True)
    id_administrador = Column(Integer(), nullable=True)
    id_estado = Column(Integer(), nullable=False)
    id_repartidor = Column(Integer(), nullable = True,default=None)
    nombre_cliente = Column(String(50), nullable = False)
    apellido_cliente = Column(String(50), nullable = False)
    direccion_cliente = Column(String(50), nullable = False)
    departamento_cliente = Column(String(50), nullable = False)
    telefono_cliente = Column(String(50), nullable = False)
    descuento = Column(Float(), nullable = True) 
    precio_total = Column(Float(), nullable = True) 
    fecha_pedido = Column(Date(), nullable = False) 
    fecha_entrega = Column(Date(), nullable = True)
    observaciones_cliente =  Column(String(), nullable = True) 
    observaciones_negocio =  Column(String(), nullable = True) 
    
    def __str__(self):
        return  " ID Pedido: " + str(self.id_pedido)
    
 #----------- SERVICIOS -----------------
 
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
        DetallePedidos.addDetallePedido(id_pedido=pedido.id_pedido,
                                        id_producto=detalle["id_producto"],
                                        cantidad=detalle["cantidad"])
    
    session.close()
    return pedido.id_pedido
    