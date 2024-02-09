#Read de la base de datos
import connection
import psycopg2
from connection import conecta

def select():
    try:
        conn = connection.conecta()
        cursor = conn.cursor()
        select = '''
        select * from pokemon
        '''
    
        cursor.execute(select)
        resultado = cursor.fetchAll()
        print(resultado)
        print("Select bien: " + select)
    except Exception as e:
        conn.commit()
        print("El error del select es: ",e) 
    finally:
        cursor.close()
        conn.close()