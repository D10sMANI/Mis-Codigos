def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

numero = int(input('Ingrese el numero a continuacion: '))
resultado = factorial(numero)

print("El factorial de", numero, "es", resultado)
