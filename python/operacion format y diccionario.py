# varias maneras de usarlo

print('{} es el primer valor y {} el segundo \n' .format(1,2))


print('En este caso alteramos el orden y el {1} aparece primero, luego el {0} \n' .format('Uno','Dos'))


nombre = 'audifonos'
x = 50.99
print('El valor de {nombre} es ', x)


print(f'El valor de {nombre.title()} es \n', x, 'Dolares por la oferta') #el .title hace que las primera letras de cada palabra sean mayusculas

diccionario = {'uno' : x, 'dos' : x.__add__(10)};
print(diccionario)

print(f'{nombre.title()} cuesta {diccionario["uno"]} dolares \n y el otro audifono cuesta {diccionario["dos"]} dolares ')
