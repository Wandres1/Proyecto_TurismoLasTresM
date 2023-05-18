from flask import Flask
from views.Taxista_views import *
from views.Usuario_views import *
from views.Cliente_views import *
from views.Administrador_views import *

app = Flask(__name__)

app.add_url_rule('/taxista', view_func = listar_taxistas)
app.add_url_rule('/crear_taxista', view_func = crear_taxista)

app.add_url_rule('/usuario', view_func = listar_usuarios)
app.add_url_rule('/crear_usuario', view_func = crear_usuario)

app.add_url_rule('/administrador', view_func = listar_administrador)
app.add_url_rule('/crear_administrador', view_func = crear_administrador)

app.add_url_rule('/usuario', view_func = listar_usuarios)
app.add_url_rule('/crear_usuario', view_func = crear_usuario)

if __name__ == '__main__':
    app.run()
