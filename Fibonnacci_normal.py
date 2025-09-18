
def fibonacci(n):
    serie = [0, 1]
    for i in range(2, n):
        serie.append(serie[-1] + serie[-2])
    return serie

fib_10000 = fibonacci(10000)

print("Primeros 10:", fib_10000[:10])
print("Último número (posición 10000):")
print(fib_10000[-1])
