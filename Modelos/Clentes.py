from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Date
from Modelos.Database.Restaurant import Restaurant 

#----------- DAO -----------------
Base = declarative_base()

class Cliente(Base):
    
    __tablename__ = 'Clientes'
    
    id_cliente =  Column(Integer(),primary_key = True, autoincrement = True)
    nombre_cliente = Column(String(50), nullable = False)
    apellido_cliente = Column(String(50), nullable = False)
    nro_documento_cliente = Column(String(50), nullable = False)
    email_cliente = Column(String(80), nullable = False, unique = True)
    telefono_cliente = Column(String(50), nullable = False)
    calle_cliente = Column(String(50), nullable = False)
    nro_calle_cliente = Column(String(50), nullable = False)
    barrio_cliente = Column(String(50), nullable = False)
    localidad_cliente = Column(String(50), nullable = False)
    password_cliente = Column(String(255), nullable = False)
    

    def __str__(self):
        return  " ID Cliente: " + str(self.id_cliente)

Base.metadata.create_all(Restaurant.getInstance().engine)
    