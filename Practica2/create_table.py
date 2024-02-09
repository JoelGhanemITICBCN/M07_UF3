#Creacion de la tabla
import connection
def createTable():
    try:
        conn = connection.conecta()
        cursor = conn.cursor()
        createTable = '''CREATE TABLE if not exists pokemon(
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(255) NOT NULL,
                        type VARCHAR(255) NOT NULL,
                        weight BIGINT NOT NULL,
                        lvl VARCHAR(255) NOT NULL,
                        height VARCHAR(255) NOT NULL
        )'''
        cursor.execute(createTable)
        conn.commit()
        print("Tabla creada bien: " + createTable)
    except Exception as e:
        print("Error al crear tabla: ",e) 
    finally:
        cursor.close()
        conn.close()