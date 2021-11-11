from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from Modelos.Database.Restaurant import Restaurant 

#----------- DAO -----------------
Base = declarative_base()
class Estado(Base):
    
    __tablename__ = 'Estados'
    
    id_estado = Column(Integer(), primary_key=True, autoincrement=True)
    descripcion = Column(String(50), nullable = False)

    
    def __str__(self):
        return  "ID: " + self.id_estado 

Base.metadata.create_all(Restaurant.getInstance().getEngine())
#----------- SERVICIO -----------------

def getEstadoById(id_estado):
    session = Restaurant.getInstance().session
    estado = session.query(Estado).filter_by(id_estado=id_estado).one()
    return estado