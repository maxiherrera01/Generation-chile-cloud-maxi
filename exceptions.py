try:
    numero = int(input("Ingrese un número entero: "))
    print(f"El número ingresado es: {numero}")
except:
    print("Error: Debe ingresar un número entero válido.")

try:
    numero = float(input("Ingrese un numero: "))
    resultado = numero / 5
    print(f"el resultado al dividir {numero} entre 5 es: {resultado}")
except ValueError:
    print("Error: ingresa un numero valido")
except ZeroDivisionError:
    print("Error: no se puede dividir entre cero")



#con funciones 

def validar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")
    return edad


# validar un correo electronico


def validar_email(email):
    if "@" not in email:
        raise ValueError("Email inválido, debe contener '@'.")
    return email
   
try:
    correo = input("Ingresa tu correo: ")
    correo_validado = validar_email(correo)
    print("Correo válido:", correo_validado)
 
except ValueError as error:
    print("Error:", error)


