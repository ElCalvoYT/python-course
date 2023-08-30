cadena1 = "Hola soy Juansi"

#----------------------------------------------------------------

# dir
#* returns a list of methods that we can use with the given object
print(dir(cadena1))

#----------------------------------------------------------------

# upper, lower, title, capitalize, count, isalpha, isalnum, isdecimal, isdigit
print(cadena1.upper())

#----------------------------------------------------------------

# Serach for substring in a string

# find
#! Case Sensitive
#* returns -1 if the substring is not found
#* returns the index of the first occurrence of the substring in the string
print(cadena1.find("Hola"))

# index
#! Case Sensitive
#! Throws an exception if the substring is not found
#* returns the index of the first occurrence of the substring in the string
print(cadena1.find("Hola"))

#----------------------------------------------------------------

# get length of a string

caracteres = len(cadena1)

print(caracteres)

#----------------------------------------------------------------

#Detect if starts or ends with a substring

#startswith
#* returns true if the string starts with the given substring
print(cadena1.startswith("Hola"))

#ensendswith
#* returns true if the string ends with the given substring
print(cadena1.endswith("Juansi"))

#----------------------------------------------------------------

#Replace a substring
#* replaces the first occurrence of the substring with the given string
#* returns a new string with the replaced substring if the substring was found
cadena_nueva = cadena1.replace("Hola", "Que tal")

#----------------------------------------------------------------

#Split a string
#* splits the string on the given separator
#* returns a list of strings

cadena1_split = cadena1.split(" ")

#----------------------------------------------------------------