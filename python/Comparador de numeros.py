# Solicite 3 numeros enteros y verifique cual es el mayor

print('******************************************************')
print(' Programa para determinar cual numero es mayor \n') 
print('****************************************************** \n ')

primero = int(input('Ingrese el primer numero \n'))
segundo = int(input('Ingrese el segundo numero \n'))
tercer = int(input('Ingrese el tercer numero \n'))

if primero > segundo and primero >tercer :
    print('El numero ',primero, ' es el mayor')
elif segundo > primero and segundo > tercer :
    print('El numero ', segundo, ' es el mayor')
else :
    print('El numero ', tercer, ' es el mayor')
print('FIN.')