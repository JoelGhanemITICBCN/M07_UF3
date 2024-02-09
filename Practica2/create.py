#insert de sql
import connection
import psycopg2
from connection import conecta
def create():
    try:
        conn = connection.conecta()
        cursor = conn.cursor()
        insert = ''' insert into pokemon (name, type,weight,lvl,height) 
                    values('pikachu','electric',12,100,1)
        '''
        cursor.execute(insert)
        conn.commit()
        print("Insert bien: " + insert)
    except Exception as e:
        print("Error al hacer el insert: ",e) 
    finally:
        cursor.close()
        conn.close()