from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer
from Modelos.Database.Restaurant import Restaurant

Base = declarative_base()

class DetallePedido(Base):
    
    __tablename__ = 'Detalle_Pedidos'
    
    id_detalle_pedido =  Column(Integer(), primary_key=True)
    id_producto = Column(Integer(), nullable=False)
    id_pedido =  Column(Integer(), nullable=True)
    cantidad = Column(Integer(), nullable = False)
    
    def __str__(self):
        return  "ID Producto: " + str(self.id_producto) + " ID Pedido: " + str(self.id_pedido)

Base.metadata.create_all(Restaurant.getInstance().engine)   
    