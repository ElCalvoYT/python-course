
#* The input() funtion returns a string value.

#----------------------------------------------------------------

# Request the name to the user

nombre = input("che maestro dame tu nombre: ")
#* Now the "nombre" variable is set to the user's name.
# for example --> nombre = John Doe

#----------------------------------------------------------------

# Request a number to the user

#! This will return an string value.
# This can cause errors like:
# "3" + "3" = "33" --> This is not correct
numero = input("che maestro dame un numero: ")

# To avoid this, we can use the "int()" function.

#* This will return an integer value.
#! does not allows decimal values.
numero = int(input("che maestro dame un numero: "))

# To avoid this, we can use the "float()" function.

#* This will return a floating point value.
numero = float(input("che maestro dame un numero: "))

#----------------------------------------------------------------

