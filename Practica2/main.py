import psycopg2
from create import create
from connection import conecta
from create_table import createTable
from select import select
try: 
   conecta()
   createTable()
   create()
   select()
except Exception as e:
   print("Error en main: ",e) 