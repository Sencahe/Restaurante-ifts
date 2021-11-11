from Modelos.Database.Restaurant import Restaurant 
from Modelos.Estados import Estado

def getEstadoById(id_estado):
    session = Restaurant.getInstance().session
    estado = session.query(Estado).filter_by(id_estado=id_estado).one()
    return estado