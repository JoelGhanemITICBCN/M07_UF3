#Read de la base de datos
import connection

def select():
        select = '''
        select * from pokemon
        '''
        connection.execute(select)
        resultados = connection.fetchall()
        if len(resultados) > 0:
            for resultado in resultados:
                print(resultado)
            else: 
                print("Esta vacio")