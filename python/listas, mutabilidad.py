# Listas se ponen con []
lista_de_compras = ['Huevos', 'Leche', 'Carne', 'Jamon']
lista_con_precios = ['Huevos', 5, 'Leche', 45, 'Carne', 220, 'Jamon', 60.5]
print(type(lista_de_compras))

print(f''' Los {lista_de_compras[0]} cuestan {lista_con_precios[1]} y el {lista_de_compras[3]} cuesta {lista_con_precios[7]}''')


# Mutabilidad las listas permiten modificar el valor de alguno de sus elementos 

lista_con_precios[1] = 6
print(f'''{lista_con_precios} \n Los {lista_con_precios[0]} ahora cuestan {lista_con_precios[1]}''')