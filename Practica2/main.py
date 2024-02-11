try: 
   import psycopg2
   from create import *
   from connection import *
   from create_table import *
   from read import *
   from update import *
   from delete import *
   connection

   def todo(): 
      print("Primero se crea la tabla")
      print("###################################################")
      createTable()
      print("Ahora hacemos el insert")
      print("###################################################")
      create()
      print("Ahora leemos los contenidos de la tabla")
      print("###################################################")
      select()
      print("Ahora actualizamos la tabla")
      print("###################################################")
      update()
      print("Volvemos a mostrar los contenidos de la tabla")
      print("###################################################")
      select()
      print("Eliminamos la tabla")
      print("###################################################")
      delete()
      print("Volvemos a mostra los contenidos de la tabla")
      print("###################################################")
      select()

   inicio = input("Quieres acceder a la creacion de la base de datos? Si/No     ")
   while inicio == 'Si':
         print()
         metodo = input("Elige (1: Crear Tabla), (2: Insertar valores), (3: Modificar Valores), (4: Borrar la tabla) (5: Ver los contenidos de la tabla), (6: Ver todas las operaciones), (7: Salir)  ")
         if metodo == '7':
            incio = 'No'
            break
         elif metodo == '1':
            createTable()
         elif metodo == '2':
            create()
         elif metodo == '3':
            update()
         elif metodo == '4':
            delete()
         elif metodo == '5':
            select()
         elif metodo == '6':
            todo()
except Exception as e:
   print("Error: ",e) 
finally:
   print("Muchas gracias por su visita, vuelva pronto")
   conn.close()