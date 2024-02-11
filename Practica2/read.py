#Read de la base de datos
#Comprobado por separado que funciona
import connection

def select():
    #query
        select = '''
        select * from pokemon
        '''
        #Ejecucion y aplicacion de la query
        connection.conection.execute(select)
        resultados = connection.conection.fetchall()
        #Si la lista no esta vacia, muestra todos los datos
        if len(resultados) > 0:
            for resultado in resultados:
                print(resultado)
        #Si esta vacia dice que esta vacia
        else: 
            print("La tabla esta vacia")