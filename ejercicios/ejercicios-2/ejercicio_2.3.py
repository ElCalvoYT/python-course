# Creando la serie de fibonacci hasta el numero dado

def fibonacci(n):
    a, b = 0, 1
    fibonacci_series = []
    for i in range(n):
        if b > n:
            return fibonacci_series
        else:
            fibonacci_series.append(b)
            a, b = b, a + b
    return fibonacci_series

fibonacci = fibonacci(100**2150)

print(fibonacci)

# Mejor manera de calcular la serie de fibonacci hasta el numero dado
# por alguna extrana rayon no funciona

primos_hasta = lambda num: list(filter(lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)), range(2, num)))

print(primos_hasta(100 ** 2150))