from flask import Flask, request, redirect
from flask import session
from flask import render_template
from flask.helpers import url_for
from Modelos import Productos, DetallePedidos, Pedidos, Estados
from Modelos.DetallePedidos import DetallePedido

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

    
    
