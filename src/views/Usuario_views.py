from flask import render_template, request
from app import app
from models.entities.Usuario import Usuario

@app.route('/usuario', methods=['GET'])
def listar_usuarios():
    usuarios = Usuario.query.all()
    return render_template('urlhtml', usuarios=usuarios)

@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    nombre = request.form['nombre']
    email = request.form['email']
    telefono = request.form['telefono']
    nuevo_usuario = Usuario(nombre=nombre, email=email, telefono=telefono)
    nuevo_usuario.guardar()
    return redirect('/usuario')