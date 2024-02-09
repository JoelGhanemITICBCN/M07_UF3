import psycopg2
from create import create
from connection import conn

try: 
   connection = conn.cursor()
   create()
except:
   print("error") 