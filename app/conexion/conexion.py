
import psycopg2

class Conexion:

    def __init__(self):
        self.__con = psycopg2.connect("dbname=db_servisoft user=postgres host=localhost password=PY_jfhp890")

    def getConexion(self):
        return self.__con


