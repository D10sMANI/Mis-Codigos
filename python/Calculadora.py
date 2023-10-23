# Calculadora de 2 numeros, pide el tipo de operacion

print('Calculadora de una sola variable\n')
print('***********************************')
print('menu de opciones')
print('*********************************** \n')

print('1.Suma \n 2.Resta \n 3.Multiplicacion \n 4.division \n 5.Division entera \n 6.Exponente \n 7.Modulo o resto \ln')
numero = int(input('Que operacion desear realizar? \n'))
if numero == 1 :
    print('La operacion es una suma \n')
    numero = int(input('Escribe el primer numero: '))
    numero += int(input('Escribe el segundo numero'))
    print('El resultado es ', numero)
elif numero == 2 :
    print('La operacion es una resta \n')
    numero = int(input('Escribe el primer numero: '))
    numero -= int(input('Escribe el segundo numero: '))
    print('El resultado es ', numero)
elif numero == 3 :
    print('La operacion es multiplicacion \n')
    numero = int(input('Escribe el primer numero: '))
    numero *= int(input('Escribe el segundo numero: '))
    print('El resultado es ', numero)
elif numero == 4 :
    print('La operacion es una division \n')
    numero = int(input('Escribe el primer numero: '))
    numero /= int(input('Escribe el segundo numero: '))
    print('El resultado es ', numero)
elif numero == 5 :
    print('La operacion es una division entera \n')
    numero = int(input('Escribe el primer numero: '))
    numero //= int(input('Escribe el segundo numero: '))
    print('El resultado es ', numero)
elif numero == 6 :
    print('La operacion es un exponente \n')
    numero = int(input('Escribe el primer numero: '))
    numero **= int(input('Escribe el segundo numero: '))
    print('El resultado es ', numero)
elif numero == 7 :
    print('La operacion es un modulo o resto \n')
    numero = int(input('Escribe el primer numero: '))
    numero %= int(input('Escribe el segundo numero: '))
    print('El resultado es ', numero)
else :
    print('numero invalido')
print('FIN.')