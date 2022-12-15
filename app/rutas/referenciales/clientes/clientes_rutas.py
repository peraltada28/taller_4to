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
@clientesmod.route('/agregar_clientes_rut', methods=['POST'])
#def frm_nacionalidad():
def agregar_clientes_rut():
    nombre_apellido = request.json['rec_nombres']
    ci_o_ruc = request.json['rec_ci_o_ruc']
    telefono = request.json['rec_telefono']
    direccion = request.json['rec_direccion']
    estado_cli = "ACTIVO"

    res = cli_model.agregar_clientes_mod(nombre_apellido, ci_o_ruc, telefono, direccion, estado_cli)

    if res:
        return jsonify({'estado': res, 'mensaje': 'se guardo exitosamente'})
        
    return jsonify({'estado': 'error', 'mensaje': 'hendy'})