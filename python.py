import psycopg2

class Connection:
    
    def __init__(self):
        self.connection = None
    
    def openConnection(self):
        try:
            self.connection = psycopg2.connect(user="postgres",
                                               password="0000",
                                               database="conteo_victimas",
                                               host="localhost", 
                                               port="5432")
        except Exception as e:
            print (e)

    def closeConnection(self):
        self.connection.close()


    grupo_victimas = """ select * from Grupo_victimas """
    calsificacion_delito = """ select * from clasificacion_delito """
    delito = """ select * from delito """
    proceso = """ select * from proceso """
    resultado = """ select * from resultado """
    ubicacion = """ select * from ubicacion """
