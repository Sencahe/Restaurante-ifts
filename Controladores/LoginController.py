from flask import request, redirect
from flask import session
from flask import render_template
from flask.helpers import url_for
from werkzeug.security import generate_password_hash, check_password_hash
from Servicios import ClienteService
from Modelos.Clentes import Cliente
from Main import app

@app.route('/login', methods = ['GET', 'POST'])
def login():

    if request.method == "POST":
        username = request.form["usuario"]
        user = ClienteService.getClienteByEmail(username)

        if user and check_password_hash(user.password_cliente, request.form["contraseña"]):
            return render_template('login2.html', user=user)
        return "ERRORRRRRRRRRRR"
    
    return render_template('login.html')

@app.route('/create_account', methods = ['GET', 'POST'])
def createAccount():

    if request.method == 'POST':
        hashed_pw = generate_password_hash(request.form["password_cliente"], method = "sha256")
        nuevoUsuario = ClienteService.addCliente(nombre_cliente = request.form["nombre_cliente"],
                                                apellido_cliente = request.form["apellido_cliente"],
                                                nro_documento_cliente = request.form["nro_documento_cliente"],
                                                email_cliente = request.form["email_cliente"],
                                                telefono_cliente = request.form["telefono_cliente"],
                                                calle_cliente = request.form["calle_cliente"],
                                                nro_calle_cliente = request.form["nro_calle_cliente"],
                                                barrio_cliente = request.form["barrio_cliente"],
                                                localidad_cliente = request.form["localidad_cliente"],
                                                password_cliente = hashed_pw)
                                                
        return redirect(url_for('login'))
    
    return render_template('/create_account.html', isUpdate=False)


