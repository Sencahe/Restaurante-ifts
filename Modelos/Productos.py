from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from Modelos.Database.Restaurant import Restaurant 

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

Base.metadata.create_all(Restaurant.getInstance().engine)

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