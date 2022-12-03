from flask import Blueprint, render_template
from app.modelos.referenciales.clientes.ClientesModel import ClientesModel

# Se crea el módulo para Blueprint
clientesmod = Blueprint("clientes", __name__, template_folder="templates")
cli_model = ClientesModel()

# Los endpoints
@clientesmod.route('/')
def index():
    items = cli_model.listarTodos()
    print(items)
    #return render_template('clientes/index.html', item = items)
    return render_template('clientes/index.html')


