#Update de la base de datos
import connection

def update():
    update = '''
        update pokemon set 
        name = 'Squirtle',
        type = 'Agua',
        weight = '80 kg',
        height = '1,1 m',
        where name = 'pikachu';
'''
    connection.execute(update)
    connection.commit()
    print(f"Se ha actualizado tu pokemon")