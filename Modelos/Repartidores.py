from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from Modelos.Database.Restaurant import Restaurant 


Base = declarative_base()
class Estados(Base):
    
    __tablename__ = 'Repartidores'
    
    id_repartidor = Column(Integer(), primary_key=True, autoincrement=True)
    nombre_repartidor = Column(String(50), nullable = False)
    apellido_repartidor = Column(String(50), nullable = False)
    telefono_repartidor = Column(String(50), nullable = False)
    
    def __str__(self):
        return  "ID: " + self.id_repartidor 

Base.metadata.create_all(Restaurant.getInstance().getEngine())