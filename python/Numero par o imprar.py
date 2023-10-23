# Codigo para saber si el numero entero es par o impar

print('****************************************************')
print('Programa para saber si el numero es par o impar')
print('***************************************************** \n')

numero = int(input('Por favor, ingrese el numero a continuacion... \n'))
num = numero % 2
if num == 0:
    print('el numero ', numero, ' es par \n')
else :
    print('el numero ', numero, ' es impar \n')
print('FIN.')