from flask import Blueprint, render_template
from app.modelos.referenciales.clientes.ClienteModel import ClienteModel

# Se crea el módulo para Blueprint
climod = Blueprint("clientes", __name__, template_folder="templates")
climod = ClienteModel()












