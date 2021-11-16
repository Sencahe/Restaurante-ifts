from Modelos.Database.Restaurant import Restaurant
from Modelos.Clentes import Cliente

def getAllClientes():
    session = Restaurant.getInstance().session
    clientes = session.query(Cliente).all()
    return clientes
    
def updateCliente(cliente:Cliente):
    session = Restaurant.getInstance().session
    session.add(cliente)
    session.commit()
    
def addCliente(nombre_cliente,apellido_cliente,nro_documento_cliente,email_cliente,telefono_cliente,calle_cliente,nro_calle_cliente,barrio_cliente,localidad_cliente,password_cliente):
    session = Restaurant.getInstance().session
    cliente = Cliente(nombre_cliente = nombre_cliente,
                        apellido_cliente = apellido_cliente,
                        nro_documento_cliente = nro_documento_cliente,
                        email_cliente = email_cliente,
                        telefono_cliente = telefono_cliente,
                        calle_cliente = calle_cliente,
                        nro_calle_cliente = nro_calle_cliente,
                        barrio_cliente = barrio_cliente,
                        localidad_cliente = localidad_cliente,
                        password_cliente = password_cliente)
    session.add(cliente)
    session.commit()
    return cliente.id_cliente

def getClienteByEmail(username):
    session = Restaurant.getInstance().session
    try:
        cliente = session.query(Cliente).filter_by(email_cliente = username).first()
        return cliente
    except Exception as e:
        print(e)
        return None
               