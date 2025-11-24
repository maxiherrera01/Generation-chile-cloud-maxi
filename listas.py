alumnos = []

alumno1 = input("Ingrese el nombre del alumno 1: ")
alumno2 = input("Ingrese el nombre del alumno 2: ")
alumno3 = input("Ingrese el nombre del alumno 3: ")
alumno4 = input("Ingrese el nombre del alumno 4: ")
alumno5 = input("Ingrese el nombre del alumno 5: ")

alumnos.append(alumno1)
alumnos.append(alumno2)
alumnos.append(alumno3)
alumnos.append(alumno4)
alumnos.append(alumno5)

print (alumnos)

# ACTUALIZAMOS CON UN NUEVO ALUMNO PARA LA POSICION 2
alumnos.insert(1, input("Ingrese el nombre del nuevo alumno para la posicion 2: "))

print (alumnos)

# ELIMINAMOS un alumno con delete

alumnos.pop(3)

print (alumnos) 


