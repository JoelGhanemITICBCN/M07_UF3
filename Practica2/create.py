#insert de sql
import connection
from connection import conecta
def create():
    conn = connection.conecta()
    cursor = conn.cursor()
    insert = ''' 
        insert into pokemon (name, type,weight,lvl,height) 
        values('pikachu','electric',12 kg,lvl 100,1 m)
                 '''
    cursor.execute(insert)
    conn.commit()
    print("Insert bien: " + insert)