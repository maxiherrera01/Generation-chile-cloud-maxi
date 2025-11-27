frutas = [
    {"nombre":"manzana", "precio": 10.99, "cantidad" : 3},
    {"nombre":"banana", "precio": 5.00, "cantidad" : 10},
    {"nombre":"cereza", "precio": .99, "cantidad" : 9}      
]
 
total_venta = 0.0
 
for fruta in frutas: #calcular el total de la venta (precio * cantidad)
    total_fruta =fruta["precio"] * fruta["cantidad"]
    total_venta = (total_venta + total_fruta )
 
print(f"Tu total de venta es : {total_venta}")


frutas = []
 
while True:
    nombre = input("Ingresa el nombre de la fruta que deseas agregar: ")
 
    if nombre == "salir": # salir cuando el usuario ingrese 'salir'
        break
    precio = float(input(f"Ingresa el precio de {nombre}: "))
 
    fruta = {
        "nombre" :nombre,
        "precio" : precio
    }
    frutas.append(fruta)
    print(f"Ingresando la fruta: {nombre} con el precio de {precio}")
 
print("Frutas ingresadas:", frutas)
 


 #for para imprimir un tikcet de compra a la terminal








