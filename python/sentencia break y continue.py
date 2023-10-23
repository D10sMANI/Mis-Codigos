# Break: Se utiliza para detener la ejecucion de una iteracion(repeticion de un segmento de codigo)

contador = 0
while contador <10 :
    contador += 1
    if contador == 5 :
        break
    print('El valor actual de la variable es: ', contador, '\n')
print('Fin del programa, la sentencia break se ha ejecutado')

# Continue: Detiene la iteracion actual y vuelve al inicio del bucle

contador = 0
while contador <10 :
    contador += 1
    if contador == 5 :
        continue
    print('El valor actual de la variable es: ', contador, '\n')
print('Fin del programa, la sentencia break se ha ejecutado')