# Speeking time calculator 

# Request text from user
frase = input("Digite uma frase: ")

# Count number of words
cantidad_palabras = len(frase.split(" "))

# Calculate time
tiempo = (cantidad_palabras / 2 / 2)

print(f"Para decir {cantidad_palabras} palabras tardarias {tiempo} segundos.")