# Se usan para comparar dos valores 

print('Introduce los numeros a comprarar \n')

valor_uno = int(input('Introduce el primer numero \n'))
valor_dos = int(input('Intoduce el segundo numero \n'))

print('Los numeros a comprarar son: ', valor_uno, ' y ', valor_dos)

if valor_uno < valor_dos:
    print('\n Es menor... \n')
if valor_uno > valor_dos:
    print('Es mayor... \n')
if valor_uno == valor_dos:
    print('Son iguales... \n')
if valor_uno <= valor_dos:
    print('Es menor o igual... \n')
if valor_uno >= valor_dos:
    print('Es mayor o igual... \n')
if valor_uno != valor_dos:
    print('Son diferentes...\n')
else :
    print('No se que ingresaste')
print('FIN')