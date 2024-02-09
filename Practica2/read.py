#Read de la base de datos
import connection
import psycopg2

def select():
        conn = connection.conecta()
        cursor = conn.cursor()
        select = '''
        select * from pokemon
        '''
    
        cursor.execute(select)
        conn.commit()
        resultados = cursor.fetchall()
        if len(resultados) > 0:
            for resultado in resultados:
                print(resultado)
            else: 
                print("Esta vacio")