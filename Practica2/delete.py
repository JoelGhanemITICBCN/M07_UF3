#query de borrado de un campo
#Comprovado por separado que funciona
import connection
def delete():
    #query 
    borra = '''
        delete from pokemon'''
    #Ejecucion y aplicacion de dicha query
    connection.conection.execute(borra)
    connection.conn.commit()
    #Mensaje de confirmacion
    print("Borrados los elementos de la tabla")