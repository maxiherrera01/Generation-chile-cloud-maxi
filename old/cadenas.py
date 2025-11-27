nombre = input ("Ingresa tu nombre")
apellido = input("lngresa tu apellido")
nombre_completo = nombre + apellido
ciudad = input ("Ingresa tu ciudad" )
mensaje = f"hola {nombre} bienvenido a {ciudad}"

print(type(nombre)) # <class 'str'>

print(mensaje.upper().replace("A", "@") )