# Los indices son numeros ordenados asociados a las variables que nos permiten identificar los elementos por su posicion

texto = 'Hola como estas' # Siempre el primer caracter es cero
print(texto[0], texto[1], texto[2], texto[3])

# Tambien se puede a la inversa comenzando desde el -1
print(texto[-6], texto[-5], texto[-4], texto[-3], texto[-2], texto[-1])


# Slicing podemos seleccionar una secuencia de elementos de una variable. [a,b] nos devuelve a  hasta el elemento previo a b (el cual esta excluido)
print(texto[0:6])