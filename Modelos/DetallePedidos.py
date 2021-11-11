from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from Modelos.Database.Restaurant import Restaurant 
from sqlalchemy.orm import sessionmaker, session

#----------- DAO -----------------
Base = declarative_base()

class DetallePedido(Base):
    
    __tablename__ = 'Detalle_Pedidos'
    
    id_detalle_pedido =  Column(Integer(), primary_key=True)
    id_producto = Column(Integer(), nullable=False)
    id_pedido =  Column(Integer(), nullable=True)
    cantidad = Column(Integer(), nullable = False)
    
    def __str__(self):
        return  "ID Producto: " + str(self.id_producto) + " ID Pedido: " + str(self.id_pedido)

Base.metadata.create_all(Restaurant.getInstance().getEngine())
    
#----------- DAO -----------------

def getDetallesPedidoByPedidoId(id_pedido):
    session = Restaurant.getInstance().session
    detallesPedido = session.query(DetallePedido).filter_by(id_pedido=id_pedido)
    return detallesPedido

def addDetallePedido(id_producto,id_pedido,cantidad):
    session = Restaurant.getInstance().session    
    session.add(DetallePedido(id_producto=id_producto,id_pedido=id_pedido,cantidad=cantidad))
    session.commit()
        
    