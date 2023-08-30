
#* To access a specific element of a (list, tuple, dictionary, set etc) we use the index starting from 0.

# Creating a list

# A list can contain multiple values of diferent types.
lista = ["Juansi", "ElCalvoYT", True, 1.70]
lista2 = list()

lista[3] = "Maquinola"

print(lista)
print(lista[1])

# ----------------------------------------------------------------

# Creating a tuple

# A tuple can contain multiple values of diferent types.
#! Tuples cannot be modified.

tupla = ("Juansi", "ElCalvoYT", True, 1.70)
tupla2 = tuple()

tupla[3] = "Maquinola" #! This will throw an error.

print(tupla)
print(tupla[1])

# ----------------------------------------------------------------

# Creating a set

# A set can contain multiple values of diferent types.
#! Set's cannot be modified.
#! Elements cannot be accessed by their index.
#! Duplicate elements are not allowed.
#* Set's allows to change the order of its alements without throwing any error.

conjunto = {"Juansi", "ElCalvoYT", True, 1.70}
conjunto2 = set()

conjunto[3] = "Maquinola"

print(conjunto)
print(conjunto[1])

#----------------------------------------------------------------

# Creating a dictionary

# A dictionary can contain multiple values of diferent types.
#* To access a specific element we use the key

diccionario = {
    'nombre': 'Juansi',
    'canal': 'ElCalvoYT',
    'activo': True,
    'altura': 1.70
}
diccionario2 = dict()

print(diccionario)
print(diccionario['nombre'])