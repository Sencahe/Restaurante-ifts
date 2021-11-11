from Modelos.Database.Restaurant import Restaurant
from Modelos.Productos import Producto

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