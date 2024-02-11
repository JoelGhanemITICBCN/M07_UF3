#query de borrado de un campo
import connection
def delete():
    borra = '''
        delete from pokemon'''
    connection.execute(borra)
    connection.commit()
    print("Borrados los elementos de la tabla")