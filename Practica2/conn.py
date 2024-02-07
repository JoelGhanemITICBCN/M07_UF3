import psycopg2

try:
#Per saber quina es la db el user i el password mirar el .yml
    conn = psycopg2.connect(
        database="postgres",
        user="admin",
        password="admin",
        host="localhost",
        port="5432"
    )
    
    #per er la connecio s utilitza el metode cursor()
    connection = conn.cursor()
    
    print(connection)
    
        # Es crea la taula users a la bd
    sql = '''CREATE TABLE USERS2(
                        user_id2 SERIAL PRIMARY KEY,
                        user_name2 VARCHAR(255) NOT NULL,
                        user_surname2 VARCHAR(255) NOT NULL,
                        user_age2 BIGINT NOT NULL,
                        user_email2 VARCHAR(255) NOT NULL
    )'''
    
    #Amb el metode execute s envia la query
    connection.execute(sql)
    #commit per fer efectius els canvis de la query a la BD
    conn.commit() 
except (Exception, psycopg2.Error) as error:
    print("Error ", error)
finally:
    conn.close()