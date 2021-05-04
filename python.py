import psycopg2

try:
    conexion = psycopg2.connect(user = "postgres",
                                password = "1234",
                                database = "covid19",
                                host = "localhost",
                                port = "5432")


    print("Conexion existosa")

    grupo_victimas = """ select * from Grupo_victimas """
    calsificacion_delito = """ select * from clasificacion_delito """
    delito = """ select * from delito """
    proceso = """ select * from proceso """
    resultado = """ select * from resultado """
    ubicacion = """ select * from ubicacion """



except Exception as e:
    print (e)

finally:
    cursor.close()
    conexion.close()
    print ("Conexion cerrada")