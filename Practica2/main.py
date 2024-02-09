import psycopg2
from create import create
from connection import conecta
from create_table import createTable
from read import select
from delete import delete
try: 
   conecta()
   createTable()
   create()
   select()
   delete()
   print("se esta borrando")
   select()
except Exception as e:
   print("Error en main: ",e) 