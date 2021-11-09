from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from Modelos.Database.Restaurant import Restaurant 


Base = declarative_base()
class Estados(Base):
    
    __tablename__ = 'Administradores'
    
    id_administrador = Column(Integer(), primary_key=True, autoincrement=True)
    nombre_administrador = Column(String(50), nullable = False)
    apellido_administrador = Column(String(50), nullable = False)
    apellido_administrador = Column(String(50), nullable = False)
    contraseña = Column(String(50), nullable = False)
    
    def __str__(self):
        return  "ID: " + self.id_administrador 