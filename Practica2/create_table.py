#Creacion de la tabla
import connection
def createTable():
        createTable = '''
                        CREATE TABLE if not exists pokemon(
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(255) NOT NULL,
                        type VARCHAR(255) NOT NULL,
                        weight varchar(255) NOT NULL,
                        lvl VARCHAR(255) NOT NULL,
                        height VARCHAR(255) NOT NULL
        )'''
        connection.execute(createTable)
        connection.commit()
        print("Tabla creada bien: " + createTable)