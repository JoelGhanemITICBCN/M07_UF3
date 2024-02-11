import psycopg2
from create import *
from connection import *
from create_table import *
from read import *
from delete import *
try: 
   conecta()
   createTable()
   create()
   select()
   delete()
   print("se esta borrando")
   select()
except Exception as e:
   print("Error: ",e) 
finally:
   conn.close()