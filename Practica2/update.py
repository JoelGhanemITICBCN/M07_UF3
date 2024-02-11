#Update de la base de datos
#Comprobado que funciona
import connection

def update():
    #Query
    update = '''
        update pokemon set 
        name = 'Squirtle',
        type = 'Agua',
        weight = 80,
        height = '1,1 m'
        WHERE name = 'pikachu';
'''
    #Ejecucion y aplicacion de la query
    connection.conection.execute(update)
    connection.conn.commit()
    #Mensja ede ocnfirmacion
    print(f"Se ha actualizado tu pokemon")