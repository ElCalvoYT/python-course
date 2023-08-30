# Create a own simple function

def saludar():
    print("Hola Juansi, como estas?")
    
saludar()

#----------------------------------------------------------------

# Create a funtion with parameters

def saludar(nombre, sexo):
    nombre = nombre.capitalize()
    sexo = sexo.lower()
    if sexo == "m":
        adjetivo = "maestro"
    elif sexo == "f":
        adjetivo = "reina"
    else:
        adjetivo = "amor"
    print(f"Hola {nombre}, mi {adjetivo} como estas?")
    
saludar("Juansi", "shsdfh")

#----------------------------------------------------------------

# Create a funtion that returns a value

def calculo(a, b):
    return a + b

resultado = calculo(2, 3) #* Now we have to sore the returned value

# Now we can print the result if we 

#----------------------------------------------------------------

