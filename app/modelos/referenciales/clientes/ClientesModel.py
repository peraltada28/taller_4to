from flask import current_app as app
from app.conexion.Conexion import Conexion

class ClientesModel:
    
    def listarTodos(self):
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cursor = con.cursor()
            cursor.execute("SELECT cli_cod, cli_nom_ape FROM public.clientes")
            items = cursor.fetchall()
            cursor.close()
            con.close()
            return items
            #return "ClientesModel > listarTodos > return"
        except:
            app.logger.error('Ha ocurrido un error al listar Clientes')