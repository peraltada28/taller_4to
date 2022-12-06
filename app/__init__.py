
from flask import Flask, render_template

app = Flask(__name__)

from app.rutas.referenciales.clientes.clientes_rutas import clientesmod

# Versión corta
# Estirar de clientes_rutas la funcion clientesmod para acortar el URL
app.register_blueprint(clientesmod, url_prefix="/clientes")