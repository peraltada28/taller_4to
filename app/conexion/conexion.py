
import psycopg2

class Conexion:

    def __init__(self):
        self.__con = psycopg2.connect("dbname=db_project user=postgres host=localhost port=5432")

    def getConexion(self):
        return self.__con


