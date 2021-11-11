from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, session

from Modelos.Database.Restaurant import Restaurant 

#----------- DAO -----------------
Base = declarative_base()

class Producto(Base):
    
    __tablename__ = 'Productos'
    
    id_producto = Column(Integer(), primary_key=True)
    nombre_producto = Column(String(50), nullable = False, unique=True)
    url_foto = Column(String(), nullable = False)
    precio = Column(Float(), nullable = False) 
    descuento = Column(Float(), nullable = False) 
    stock = Column(Integer(), nullable = False)
    
    def __init__(self,cantidad=1):
        self.cantidad = cantidad
    
    def __str__(self):
        return  "ID: " + str(self.id_producto) + " NOMBRE: " + self.nombre_producto 
    
#--------- SERVICIOS ------------ 

def getAllProductos():
    session = Restaurant.getInstance().session
    productos = session.query(Producto).all()
    return productos

def getProductoById(id:int):
    session = Restaurant.getInstance().session
    try:
        producto = session.query(Producto).filter_by(id_producto = id).one()
        return producto
    except Exception as e:
        print(e)
        return None
    
    
"""
session = Restaurant.getInstance().session
productos = session.query(Producto).all()
for producto in productos:
    print(producto)
    
producto = Producto(nombre_producto = 'Milanesa de Carpincho',
                    url_foto = 'Vistas/img/MilanesaCarpincho.jpg',
                    precio = 500,
                    descuento = 0,
                    stock = 10)

print (producto)

"""