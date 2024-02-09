import psycopg2
#from create import create
from connection import conecta
from create_table import createTable
try: 
   conecta()
   createTable()
   #create()
except Exception as e:
   print("Error en main: ",e) 