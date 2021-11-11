from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Date
from Modelos.Database.Restaurant import Restaurant 

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

Base.metadata.create_all(Restaurant.getInstance().engine)
    