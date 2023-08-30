# Preguntar la cantidad de alumnos presentes en el grupo.
def getAlumnos():
    alumnos = int(input("Ingrese la cantidad de alumnos: "))
    return alumnos

# Crea una lista con los nombres de los alumnos y la edad
def createClass(alumnos):
    clase = []
    for i in range(0, alumnos):
        nombre = input("Ingrese el nombre del alumno: ")
        edad = int(input("Ingrese la edad del alumno: "))
        alumno = (nombre, edad)
        clase.append(alumno)
    return clase

# Obtiene los substitutos segun la edad
def getSubstitutes(clase):
    clase.sort(key=lambda x: x[1])
    asistent = clase[0][0]
    teacher = clase[-1][0]
    return asistent, teacher

# ejecutando las funciones y mostrando quien es el profesor y la asistente
getAlumnos = getAlumnos()
clase = createClass(getAlumnos)
asistent, teacher = getSubstitutes(clase)

print(f"La asistente es: {asistent}")
print(f"El profesor es: {teacher}")

