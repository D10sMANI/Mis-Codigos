# Permiten agrupar condiciones logicas dentro de una misma condicion

#disyuncion
print('disyuncion(or) \n')
palabra = input(' Para cumplir con la condicion escribe "si" o "yes" ')
if palabra =="si" or palabra == "yes":
    print('/n La condicion se ha cumplido \n')
else : 
    print('La condicion no se ha cumplido \n')


#conjuncion
print('conjuncion (and) \n')
num = int(input('Escribe un numero mayor a 3 y menor que 7 \n'))
if num > 3 and num < 7 :
    print('El numero ', num,' Cumple con la condicion \n')
else :
    print(' El numero', num, ' no cumple con la condicion \n' )
print('FIN')


#Negacion
print('Negacion (not)')
num_uno = int(input('Introduce un numero igual a 5 \n'))
if not num_uno == 5 :
    print (' El numero no es igual a 5 y cumple con la condicion \n')
else :
    print('El numero es igual a 5 y no cumple con la condicion')

