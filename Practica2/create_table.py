#Creacion de la tabla
#Comprobado que funciona por separado
import connection
def createTable():
        #query
        dropTable = '''DROP TABLE IF EXISTS pokemon'''
        createTable = '''
                        CREATE TABLE if not exists pokemon(
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(255) NOT NULL,
                        type VARCHAR(255) NOT NULL,
                        weight BIGINT NOT NULL,
                        lvl VARCHAR(255) NOT NULL,
                        height VARCHAR(255) NOT NULL
        )'''
        #Ejecucion de la query con el commit para que se aplique
        connection.conection.execute(dropTable)
        connection.conection.execute(createTable)
        connection.conn.commit()
        print("Tabla creada bien: " + createTable)