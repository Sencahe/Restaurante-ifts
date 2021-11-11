from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from Modelos.Database.Restaurant import Restaurant 

#----------- DAO -----------------
Base = declarative_base()
class Estado(Base):
    
    __tablename__ = 'Estados'
    
    id_estado = Column(Integer(), primary_key=True, autoincrement=True)
    descripcion = Column(String(50), nullable = False)

    
    def __str__(self):
        return  "ID: " + self.id_estado 

Base.metadata.create_all(Restaurant.getInstance().engine)
