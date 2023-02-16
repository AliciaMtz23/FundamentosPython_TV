# Esto es de un comentario 
def nuevoTema(tema):
   print("============",tema,"=======")

if __name__ == "__main__":
   print("=====Operadores aritmeticos =====")
   print("Operador de division entera (10 // 3): ", 10//3)
   print("Operador de potencias (5 ** 5):", 5 ** 5)
   print("Operador de cambio de signo (-5): ", -5)


   print("=======Operadores lógicos======")
   print("Operador and (True and False): ", True and False)
   #Actividd: Mostrar las tablas de verdad de los operador logicos.
   print("Operador and (False and True): ", False and True)
   print("Operador and (True and true): ", True and True)
   print("Operador and (False and False): ", False and False)

   print("Operador or (True or False): ", True or False)
   print("Operador or (False or True): ", False or True)
   print("Operador or (True or true): ", True or True)
   print("Operador or (False or False): ", False or False)

   print("Operador  (True not false): ", not True)
   print("Operador  (False not True): ", not False)
  

   print("======Operadores de comparacion=======")
   print("operador 2==3", "2==3")
   #Actividad: Agregar los demas operaores de comparacion
   print("operador ")
  
   nuevoTema("Enteros")
   w =105
   x = 2074074873847821
   y = -345
   z = 0b00110011 #Entero en binario.
   h = 0xffa #entero en hexadecimal.

   print(w, type(w))
   print(x, type(x))
   print(y, type(y))
   print(z, type(z))
   print(h, type(h))

   nuevoTema("Flotantes")
   x = 1297.5
   print(x, type(x))
   y = 0.052829
   print(y, type(y))

   nuevoTema("Numeros Complejos")
   x = -46j
   y = 12 + 45j
   z = 2j

   print(x, type(x))
   print(y, type(y))
   print(z, type(z))

   nuevoTema("Listas")
   a = [10, 20.5, "python list"]
   print(a)
   a = ["lista2", 45, 16.3j]
   print(a)
   print(a[2])
   a[1] = 34.6
   print(a)

   nuevoTema("Tuplas")
   t = (25, "tupla", 5.6)
   print(t)
   print(t[1])
   #t[0] = "modificado" #OPERACION NO PERMITIDA EN TUPLAS.
   #print(t)

   nuevoTema("Conjuntos")
   c = {50, 20, 10, 4, 8 ,50} #los elementos del conjunto son unicos no se pueden repetir
   print(c) #los conjuntos no estan definidos el orden 

   nuevoTema("Diccionarios") #no tienen orden
   d = {1: "valor2", "2":45}
   print(d, type(d))
   print(d["2"])
   print(d[1])

   nuevoTema("Cadenas")
   cadena1 = "cadena entre comillas dobles"
   print(cadena1)
   cadena2 = 'cadena entre comillas sencillas'
   print(cadena2)
   cadena3 = '''cadena de
      varias 
   lineas'''
   print(cadena3)
