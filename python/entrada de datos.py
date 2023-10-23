palabra = input("Introduce una palabra") # con input solicita que el usuario ponga algo
num_int = int(input("Introduce un numero entero"))  # con int se va a guardar como numero entero
num_float = float(input("Introduce un numero flotante"))
num_complex = complex(input("Intoduce un numero complejo"))
print("string: ", palabra)
print("Entero: ", num_int)
print("flotante:", num_float)
print("numero complejo", num_complex)


#Practica

nombre = input("¿Cual es tu nombre?")
print("hola", nombre,", vamos a sumar.")

num_uno = int(input("Por favor introduce tu primer valor:"))
num_dos = int(input("Por favor introduce tu segundo valor:"))

resultado = num_uno + num_dos

print(nombre, "el resultado de la suma es:", resultado)
