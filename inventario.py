name="Sistema Inventario"
print(name.center(30,"="))
print("Bienvenido al Sistema")

productos=[]

def Agregar():
      while True:
       nombre=input_obligatorio("Ingrese Nombre Producto: ")
       precio=float (input_obligatorio("Ingrese Precio Producto: "))
       cantidad= input_numero("Ingrese Cantidad Producto: ")
       producto ={"nombre":nombre, "precio":precio,"cantidad":cantidad,"Total":precio*cantidad}
       productos.append(producto)
       print("Producto Agregado Correctamente")
       while True:
         seleccion=input("Desea agregar otro Producto: ").lower()
         if seleccion=="si":
          break
         elif seleccion=="no":
          return
         else: 
          print("Opcion Incorrecta escriba si o no")
          

def mostrar(): 
  if not productos:
    print("No Existen Productos")
  else:
    for i in productos: 
     print("\n------ Producto ------")
     for nombre,valor in i.items():
       print(nombre,":",valor)

def total():
    total_inventario=0
    for i in productos:
       total_inventario += i ["Total"]
    print("\n----------Total Inventario---------")
    print(f" El total inventario es {total_inventario}")

def buscar():
  if not productos:
    print("\n Inventario Vacio")
    return
  producto=input_obligatorio("Ingrese Producto a Buscar: " )
  resultados=buscar_log(producto)
  if not resultados:
    print("\n Producto No Encontrado")
    return
  for lista in resultados:
    info_producto=obtener_producto(lista)
    print("\n" + "=" * 30)
    print (info_producto)
    print("=" * 30)
    
def input_obligatorio(mensaje):
  while True:
    valor=input(mensaje).strip().title()
    if valor:
     return valor
    else:
      print("Este Campo es Obligatorio")
  
def buscar_log(producto):
  resultados=[]
  for info_p in productos:
    if info_p["nombre"]==producto:
      resultados.append(info_p)
  return resultados
  
def obtener_producto(lista):
  campos=[
    f"Nombre:{lista['nombre']}",
    f"Precio:{lista['precio']}",
    f"Cantidad:{lista['cantidad']}",
    f"Total:{lista['Total']}"
    ]
  info_producto="\n".join(campos)
  return(info_producto)

def eliminar():
  if not productos:
    print("Inventario Vacio")
    return
  producto=input_obligatorio("Ingrese Producto a Eliminar")
  resultados=buscar_log(producto)
  for lista in resultados:
    info_producto=obtener_producto(lista)
    print(info_producto)
  while True:
    confirmar=input("Eliminar producto Si/No: ").title()

    if confirmar=="Si":
      productos.remove(lista)
      print(f"Producto:{producto} Eliminado Correctamente")
      return
    elif confirmar=="No":
      print("Operacion Cancelada")
      return
    else:
      print("Opcion Incorrecta Seleccion Si/No")
      confirmar=input("Eliminar producto Si/No: ").title()
  
def input_numero(mensaje):
  while True:
    valor=input(mensaje).strip()
    if valor.isdigit():
      return int(valor)
    else:
      print("Ingrese Solo Numeros")      


menu=[
      "1. Agregar Producto",
      "2. Mostrar Productos",
      "3. Calcular Todo el inventario",
      "4. Buscar",
      "5. Eliminar Producto",
      "6. Salir"
      ]
def menu_():
 continuar=True
 while continuar:
   print("\n" + "=" * 30)
   for opcion in menu:
      print(opcion)
   print("=" * 30)   
   eleccion=input_numero("Seleccione una opcion: ")
   if eleccion==1:
      Agregar()
   elif eleccion==2:
      mostrar()
   elif eleccion==3:
      total()
   elif eleccion==4:
     buscar()
   elif eleccion==5:
     eliminar()
   elif eleccion==6:
      print("Saliendo de Sistema")
      continuar=False
   else:
     print("\n Opcion Incorrecta, intente de nuevo ") 
menu_()        
   


    


