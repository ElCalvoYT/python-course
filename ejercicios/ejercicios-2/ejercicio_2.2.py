# generate prime numbers until passed parameter

def prime_check(n):
    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True

def primos_hasta(n):
    primeNumbers = []
    for i in range(3, n + 1):
        resultado = prime_check(i)
        if resultado == True:
            primeNumbers.append(i)
    return primeNumbers

resultados = primos_hasta(100000)

print(resultados)