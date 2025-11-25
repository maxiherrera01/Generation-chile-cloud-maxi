# las funciones sirven para encapsular bloques repetitivos de codigo y reutilizarlos cuando sea necesario
# se crean uilizando la palabra clave "def", seguida del nombre de la funcion y parentesis. (por ejemplo: def hola():)
#los argumentos o parametros se colocan dentro de los parentesis.
#pueden devolver un valor utilizando la palabra clave "return".

#ejemplo de una funcion que no recibe parametros y no devuelve ningun valor

def saludo(nombre, edad):
    total_dias = calculo_anios_por_edad(edad)
    print(f"Hola, {nombre}! que bueno tenerte de regreso, han pasado {total_dias} desde que naciste")
 
def calculo_anios_por_edad(edad):
    dias_anio = 365
    dias_totales = dias_anio * edad
    return dias_totales
 
saludo(
    input("Ingresa tu nombre: "), 
    int(input("Ingresa tu edad: "))
)