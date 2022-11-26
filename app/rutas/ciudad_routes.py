
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

#Se modularizan las vistas de ciudades
ciudadmod = Blueprint("ciudad", __name__, template_folder="templates")

#Lugar de las vistas
@ciudadmod.route()
def index():
    render_template(clientes)












