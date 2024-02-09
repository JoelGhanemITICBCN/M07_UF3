#Read de la base de datos
import psycopg2

select = '''
    select * from pokemon
'''