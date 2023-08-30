# Otros cursos

otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_prom = 4

otros_cursos_crudo_prom = 5

# Dalto curso

dalto_curso = 1.5

dalto_curso_crudo = 3.5

# Soluciones

# a)

solucion_min = 100 - ((dalto_curso / otros_cursos_min) * 100)
solucion_max = 100 - ((dalto_curso * 1000 // otros_cursos_max) / 10)
solucion_prom = 100 - ((dalto_curso / otros_cursos_prom) * 100)

# Mostrando resultados

print(f"El curso de dalto es un: {solucion_min}% mas rapido que el mas rapido de los otros cursos.")
print(f"El curso de dalto es un: {solucion_max}% mas rapido que el mas lento de los otros cursos.")
print(f"El curso de dalto es un: {solucion_prom}% mas rapido que el promedio de los otros cursos.")

#----------------------------------------------------------------

print("\n")
print("-" * 66)
print("\n")

#----------------------------------------------------------------

# b)

solucion_crudo_prom = 100 - ((otros_cursos_prom * 1000 // otros_cursos_crudo_prom) / 10)
solucion_dalto_crudo_prom = 100 - ((dalto_curso * 1000 // dalto_curso_crudo) / 10)

# Mostrando resultados

print(f"Otros cursos eliminan un promedio de un {solucion_crudo_prom}% de tiempo vacio")
print(f"Este curso elimino un {solucion_dalto_crudo_prom}% de tiempo vacio")

#----------------------------------------------------------------

print("\n")
print("-" * 66)
print("\n")

#----------------------------------------------------------------

# c)

print(f"Ver 10 horas de este curso equivalen a ver: {otros_cursos_prom * 100 // dalto_curso / 10} de otros cursos")
print(f"Ver 10 horas de otros cursos equivalen a ver: {dalto_curso * 100 // otros_cursos_prom / 10} de este curso")