# Podemos inicializar una lista de numeros a traves de la funcion llamada range(a,b,in)
    # a es el limite inferior de la secuencia de numeros
    # b es el limite superior (se excluye)
    # in es la unidad de incremento (argumento opcional)

numeros = range(0,20,2)
lista_numeros = list(numeros)
print(f'{numeros} {lista_numeros}')

# append agrega un elemento mas al final de la lista
lista_numeros.append(4)
print(lista_numeros)

# Tambien se puede concatenar con +
str(lista_numeros)
lista_numeros + [23, 52, 14, 55, 'hola', 'bye', 'hello']
print(lista_numeros)

# con el termino in podemos comprobar si algun valor existe dentro de una lista
if 23 in lista_numeros :
    print('Si')
else :
    print('no')

# Slicing para actualizar los valores de la lista