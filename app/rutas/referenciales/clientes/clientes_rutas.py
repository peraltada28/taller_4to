from flask import Blueprint, render_template

clientesmod = Blueprint("clientes", __name__, template_folder="templates")

#Los edpoints
@clientesmod.route('/')
def index():
    #retornar algo
    return "Se realizara el index de clientes"
    




