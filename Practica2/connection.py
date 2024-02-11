#conexion a la base de datos
import psycopg2

conn = psycopg2.connect(
    database="postgres",
    user="admin",
    password="admin",
    host="localhost",
    port="5432"
)

conection = conn.cursor()
print(f"Se ha conectado, {conection}")