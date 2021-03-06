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
    
def updateProducto(producto:Producto):
    session = Restaurant.getInstance().session
    session.add(producto)
    session.commit()
    
def addProducto(nombre_producto,precio:float,stock:int,descuento:float,url_foto):
    session = Restaurant.getInstance().session
    producto = Producto(nombre_producto=nombre_producto,
                        precio=precio,
                        stock=stock,
                        descuento=descuento,
                        url_foto=url_foto)
    session.add(producto)
    session.flush()
    session.commit()
    return producto.id_producto

def deleteProductoById(id:int): 
    session = Restaurant.getInstance().session
    producto = session.query(Producto).filter_by(id_producto = id).one()
    session.delete(producto)
    session.commit()
               