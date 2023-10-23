# Define una variable edad y asigne un valor entero
# Muestre valor en pantalla, define otra variable edad_cadena que contenga el valor de la edad como cadena de caracteres 
# Compruebe el tipo de variable, calcula la edad que tendria en el year 2035

#1
edad = 20 
print(edad)
edad_cadena = str(edad)
print(type(edad_cadena))
edad += 11
print(edad)

#2 cadena hace que se pueda cambiar la posicion de los caracteres
cadena = 'atropo leunam, 01'
cadena_volteada = cadena [::-1] 
print(cadena_volteada[4::], 'ha sacado un ', cadena_volteada[:2])


#Verifica que si la cadena de texto introducida es mayor o igual a 3, ademas de menor o igual a 12 (mostrar solo true or false)
cadena = input('Escribe la frase que quieres ingresar \n')
print('La cadena igresada es mayor o igual a 3 y menor o iguala 12?', len(cadena) >= 3 and len(cadena) <= 12)


