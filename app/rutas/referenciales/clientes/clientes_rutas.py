from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from markupsafe import escape
from app.modelos.referenciales.clientes.ClientesModel import ClientesModel

# Se crea el módulo para Blueprint
clientesmod = Blueprint("clientes", __name__, template_folder="templates")
cli_model = ClientesModel()

# Los endpoints
@clientesmod.route('/')
def index():
    items = cli_model.listarTodos()
    print(items)
    return render_template('clientes/index.html', items_rutas = items)


#@nacmod.route('/frm_nacionalidad')
@nacmod.route('/form_clientes')
#def frm_nacionalidad():
def form_clientes():
    id = request.args.get('id')
    descripcion = request.args.get('descripcion')
    #return render_template('nacionalidad/frm_nacionalidad.html', nac={ 'id': id, 'descripcion': descripcion })
    return render_template('nacionalidad/form_clientes.html', nac={ 'id': id, 'descripcion': descripcion })