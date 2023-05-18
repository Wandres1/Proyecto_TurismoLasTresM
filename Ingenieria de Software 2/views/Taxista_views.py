from flask import render_template, request
from app import app
from models.Taxista import Taxista

@app.route('/taxista', methods=['GET'])
def listar_taxistas():
    taxistas = Taxista.query.all()
    return render_template('urlhtml', taxistas=taxistas)

@app.route('/crear_taxista', methods=['POST'])
def crear_taxista():
    nombre = request.form['nombre']
    email = request.form['email']
    telefono = request.form['telefono']
    nuevo_taxista = Taxista(nombre=nombre, email=email, telefono=telefono)
    nuevo_taxista.guardar()
    return redirect('/taxista')