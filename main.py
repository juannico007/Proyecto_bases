from python import Connection
import sentencias as sql

a = -1
while(a != 0):

    print("1: datos grupo victimas")
    print("2: datos clasificacion delito")
    print("3: datos delito")
    print("4: datos proceso")
    print("5: datos resultado")
    print("6: analisi 1")
    print("7: analisi 2")
    print("8: analisi 3")
    print("9: analisi 4")
    print("0: cerrar programa")
    a = int(input("Escriba un numero del indice: "))

    if(a == 1):
        #datos grupo victimas 
        con = Connection()
        con.openConnection()


        cursor = con.connection.cursor()
        cursor.execute(sql.grupo_victimas())
        victimas = cursor.fetchall()
        print("*** Grupo victimas ***")
        for victima in victimas:
            print("ID_GRUPO: ", victima[0])
            print("NUMERO_VICTIMAS: ", victima[1])
            print("EDAD: ", victima[2])
            print("GENERO: ", victima[3])
            print("PAIS_DE_NACIMIENTO: ", victima[4])
            print()

        con.closeConnection()

    elif(a == 2):
        #datos clasificacion_delito

        con = Connection()
        con.openConnection()

        cursor = con.connection.cursor()
        cursor.execute(sql.clasificacion_delito())
        clasificacion = cursor.fetchall()
        print("*** Clasificacion delito ***")
        for clasifica in clasificacion:
            print("DELITO_ESPECIFICO: ", clasifica[0])
            print("GRUPO: ", clasifica[1])
            print()

        con.closeConnection()

    elif(a == 3):
        #datos delito
        con = Connection()
        con.openConnection()

        cursor = con.connection.cursor()
        cursor.execute(sql.delito())
        delitos = cursor.fetchall()
        print("*** Delito ***")
        for delito in delitos:
            print("ID_DELITO: ", delito[0])
            print("ARTICULO: ", delito[1])
            print("H_D_C: ", delito[2])
            print("HECHO: ", delito[3])
            print("ANIO_HECHO: ", delito[4])
            print("CONEXO: ", delito[5])
            print("MUNICIPIO: ", delito[6])
            print("DEPARTAMENTO: ", delito[7])
            print("DELITO_ESPECIFICO_CLASIFICACION_DELITO: ", delito[8])
            print("ID_PROCESO_PROCESO: ", delito[9])
            print("ID_GRUPO_GRUPO_VICTIMAS: ", delito[10])
            print()

        con.closeConnection()

    elif(a == 4):
        #datos proceso
        con = Connection()
        con.openConnection()

        cursor = con.connection.cursor()
        cursor.execute(sql.proceso())
        procesos = cursor.fetchall()
        print("*** Proceso ***")
        for proceso in procesos:
            print("ID_PRCEOSO: ", proceso[0])
            print("ESTADO_ACTIVIDAD: ", proceso[1])
            print("ETAPA: ", proceso[2])
            print("SECCION: ", proceso[3])
            print("IMPUTACION: ", proceso[4])
            print("ACUSACION: ", proceso[5])
            print("ANIO_ENTRADA: ", proceso[6])
            print("ANIO_DENUNCIA: ", proceso[7])
            print("ID_RESULTADO_RESULTADO: ", proceso[8])
            print()

        con.closeConnection()

    elif(a == 5):
        #datos resultado
        con = Connection()
        con.openConnection()

        cursor = con.connection.cursor()
        cursor.execute(sql.resultado())
        resultados = cursor.fetchall()
        print("*** Resultado ***")
        for resultado in resultados:
            print("ID_RESULTADO: ", resultado[0])
            print("CONDENA: ", resultado[1])
            print("CAPTURA: ", resultado[2])
            print("A_O_I: ", resultado[3])
            print("REPTURA: ", resultado[4])
            print()

        con.closeConnection()

    elif(a == 6):
        #datos analisis1

        con = Connection()
        con.openConnection()

        cursor = con.connection.cursor()
        cursor.execute(sql.analisis1())
        analisis1 = cursor.fetchall()
        print("*** Analisis1 ***")
        for analisis in analisis1:
            print("DEPARTAMENTO: ", analisis[0])
            print("NUMERO_CASOS: ", analisis[1])
            print()

        con.closeConnection()

    elif(a == 7):
        #datos analisis2

        con = Connection()
        con.openConnection()

        cursor = con.connection.cursor()
        cursor.execute(sql.analisis2())
        analisis2 = cursor.fetchall()
        print("*** Analisis2 ***")
        for analisis in analisis2:
            print("Grupo: ", analisis[0])
            print("NUMERO_CASOS: ", analisis[1])
            print()

        con.closeConnection()

    elif(a == 8):
        #datos analisis3

        con = Connection()
        con.openConnection()

        cursor = con.connection.cursor()
        cursor.execute(sql.analisis3())
        analisis3 = cursor.fetchall()
        print("*** Analisis1 ***")
        for analisis in analisis3:
            print("ETAPA: ", analisis[0])
            print("NUMERO_CASOS: ", analisis[1])
            print()

        con.closeConnection()

    elif(a == 9):
        #datos analisis4

        con = Connection()
        con.openConnection()

        cursor = con.connection.cursor()
        cursor.execute(sql.analisis4())
        analisis4 = cursor.fetchall()
        print("*** Analisis4 ***")
        for analisis in analisis4:
            print("GENERO: ", analisis[0])
            print("CONDENA: ", analisis[1])
            print("NUMERO_CASOS: ", analisis[2])
            print()

        con.closeConnection()

    elif (a == 0):

        print("Vuelva pronto")
    else:
        print("Escriba un numero valido")

