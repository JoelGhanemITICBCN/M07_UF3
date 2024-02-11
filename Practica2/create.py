#insert de sql
#Comprobado que funciona por separado
import connection
def create():
    #query
    insert = ''' 
        insert into pokemon (name, type,weight,lvl,height) 
        values('pikachu','electric',12,'lvl 100','1 m')
                 '''
    #Ejecucion y aplicacionn de dicha query
    connection.conection.execute(insert)
    connection.conn.commit()
    #Mensaje de todo okei
    print("Insert bien: " + insert)