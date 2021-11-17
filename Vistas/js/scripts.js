/*!
* Start Bootstrap - Shop Homepage v5.0.4 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project


//validaciones del formulario de alta de usuario

function validarForm() {

    var regex = new RegExp('^[A-Z\u00E0-\u00FC]+$', 'i'); //expresion regular para validar solo letras y acentos
    var regex2 = new RegExp(/(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])/)//expresion regular para validar correo
    var regex3 = new RegExp('^[A-Z0-9]+$', 'i'); //expresion regular para validar solo letras y números
    var regex4 = new RegExp(/^[0-9]{7,8}$/); //expresion regular para validar solo números
    var regex5 = new RegExp(/^[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]{8,15}$/); //expresion regular para validar


    function validaNombre() {

        var your_name = document.getElementById("nombre").value;
        var elemento = document.getElementById("nombre");

        if (regex.test(your_name) && (your_name != "null")) {
            elemento.className = "form-control";
            return true;
        }
        else {
            elemento.className += " erro";
            alert("Ingrese un nombre válido");
            return false;
        }
    }

    function validaApellido() {

        var your_surname = document.getElementById("apellido").value;
        var elemento = document.getElementById("apellido");

        if (regex.test(your_surname) && (your_surname != "null")) {
            elemento.className = "form-control";
            return true;
        }
        else {
            elemento.className += " erro";
            alert("Ingrese un apellido válido");
            return false;
        }
    }

    function validaDni() {

        var your_dni = document.getElementById("nro_documento").value;
        var elemento = document.getElementById("nro_documento");

        if (regex4.test(your_dni) && (your_dni != "null") && (your_dni > 0 && your_dni <= 99999999)) {
            elemento.className = "form-control";
            return true;
        }
        else {
            elemento.className += " erro";
            alert("Ingrese un documento v&aacute;lido");
            return false;
        }
    }

    function validaMail() {

        var your_email = document.getElementById("email").value;
        var elemento = document.getElementById("email");

        if (regex2.test(your_email) && (your_email != "null")) {
            elemento.className = "form-control";
            return true;
        }
        else {
            elemento.className += " erro";
            alert("Ingrese una dirección de correo válida");
            return false;
        }
    }

    function validaPass() {

        var your_pass = document.getElementById("password").value;
        var your_passb = document.getElementById("password2").value;
        var elemento = document.getElementById("password");
        var elemento2 = document.getElementById("password2");

        if (your_pass === your_passb) {
            if (regex5.test(your_pass) && (your_pass != "null")) {
                elemento.className = "form-control";
                return true;
            } else {
                elemento.className += " erro";
                alert("La contraseña debe tener entre 8 y 15 caracteres");
                return false;
            }
        } else {
            elemento2.className += " erro";
            alert("La contraseña no coincide");
            return false;
        }
    }


    if ((validaNombre() == true) && (validaApellido() == true) && (validaDni() == true) && (validaMail() == true) && (validaPass() == true)) {
        return true;
    }
    else
        return false;
}