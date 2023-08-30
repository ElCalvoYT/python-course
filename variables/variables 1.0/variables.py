
# Declaring a variable, this can be a string, a number, a boolean, a list, a tuple, a dictionary, a function, a class etc...
nombre = "Juansi"

# Redeclaring a variable
nombre = "Pedro" #* This is the same variable but we changed its value.

# Printing out the variable.
print(nombre)


#----------------------------------------------------------------

# Declaring a int variable "numero" and adding "1" to it.

#! This is not the best waz to do this, but it works.
numero = 10
numero = 10 + 1

#Instead do this:
numero = 10
numero += 1 #* This is the same as: "numero = 10 + 1", but better.
numero -= 1 #* You can also (subtract, divide, rest, multiply etc...) by using this method.

#----------------------------------------------------------------

# Concatening strings.

nombre = "Juansi"
# nombre = 5
# nombre = True | False
#! If we try to redeclare the string "nombre" variable, to another type, we will get an error.

bienvenida = "Hola " + nombre + " como estas?"
print(bienvenida)



#* Using "f-sting we will avoid this error".

nombre = "Juansi"
bienvenida = f"Hola {nombre} como estas?"
print(bienvenida)

# Delete a variable. n
del nombre
print(nombre) #! This will throw an error.

#----------------------------------------------------------------

# Membership operators, Operadores de pertenencia.

#! Case sensitive.

print("ola" in bienvenida) #* This will return True if "Juansi" is found in string or False if not.
print("pedro" not in bienvenida) #* This will return Tr ue if "Pedro" is not found in string or False if it is found.

#----------------------------------------------------------------

