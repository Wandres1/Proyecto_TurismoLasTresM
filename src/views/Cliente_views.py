from flask import render_template, request
from app import app
from models.entities.Cliente import Cliente

@app.route('/cliente', methods=['GET'])
def listar_cliente():
    clientes = Cliente.query.all()
    return render_template('urlhtml', taxistas=clientes)

@app.route('/crear_cliente', methods=['POST'])
def crear_taxista():
    nombre = request.form['nombre']
    email = request.form['email']
    telefono = request.form['telefono']
    nuevo_cliente = Cliente(nombre=nombre, email=email, telefono=telefono)
    nuevo_cliente.guardar()
    return redirect('/cliente')