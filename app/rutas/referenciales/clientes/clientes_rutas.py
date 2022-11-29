from flask import Blueprint, render_template
from app.modelos.referenciales.clientes.ClientesModel import ClientesModel

# Se crea el módulo para Blueprint
nacmod = Blueprint("nacionalidad", __name__, template_folder="templates")
cli_model = ClientesModel()

# Los endpoints
@nacmod.route('/')
def index():
    items = cli_model.listarTodos()
    print(items)
    return render_template('clientes/index.html', items=items)


