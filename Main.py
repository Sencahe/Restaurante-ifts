from flask import Flask

app = Flask(__name__, template_folder = 'Vistas',static_folder='Vistas')
app.secret_key = "SecretKey"

from Controladores.HomeController import *
from Controladores.CarritoController import *
from Controladores.PedidoController import *
from Controladores.LoginController import *
from Controladores.ProductoController import *

#----------------------- RUN -----------------------

if __name__ == '__main__':
    app.run(debug=True,port=8000)

    
    
