from flask import current_app as app
import psycopg2
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

    def agregar_clientes_mod(self, nombre_apellido, ci_o_ruc, telefono, direccion, estado):
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cursor = con.cursor()
            cursor.execute("INSERT INTO public.clientes(cli_nom_ape, cli_ruc_ci, cli_tel, cli_dir, cli_est) VALUES (%s,%s,%s,%s,%s)",(nombre_apellido, ci_o_ruc, telefono, direccion, estado,))
            #aqui se confirma la transaccion SQL
            con.commit()
            cursor.close()
            
            return True
        except (Exception, psycopg2.DatabaseError) as error:
            app.logger.error(f'Ha ocurrido un error al INSERTAR, mensaje= {error}')