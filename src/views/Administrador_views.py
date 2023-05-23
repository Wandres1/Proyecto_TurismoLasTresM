from flask import render_template, request
from app import app
from models.entities.Administrador import Administrador

@app.route('/administrador', methods=['GET'])
def listar_administrador():
    administradores = Administrador.query.all()
    return render_template('urlhtml', taxistas=administradores)

@app.route('/crear_administrador', methods=['POST'])
def crear_administrador():
    nombre = request.form['nombre']
    email = request.form['email']
    telefono = request.form['telefono']
    nuevo_administrador = Administrador(nombre=nombre, email=email, telefono=telefono)
    nuevo_administrador.guardar()
    return redirect('/administrador')