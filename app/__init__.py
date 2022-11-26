
from flask import Flask, render_template

app = Flask(__name__)

from app.rutas.referenciales.clientes.clientes_rutas import clientesmod

# Versión corta
app.register_blueprint(clientesmod, url_prefix="/clientes")