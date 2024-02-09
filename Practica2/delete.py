#query de borrado de un campo
import connection
def delete():
    conn = connection.conecta()
    cursor = conn.cursor()
    borra = '''
        delete from pokemon'''
    cursor.execute(borra)
    conn.commit()
    print("Borrando")