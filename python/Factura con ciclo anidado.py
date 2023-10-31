c = input('Ingrese si para iniciar a facturar \n')
while (c == 'SI' or c == 'Si' or c == 'sI' or c == 'si'):
    contador = 0
    acumulado = 0
    nombre = input('Ingrese su nombre \n')
    cantidad = int(input('Ingrese la cantidad de productos que se va a llevar \n'))
    for i in range(cantidad):
        contador += 1
        print('Precio del producto', contador,'\n')
        precio = float (input(' '))
        acumulado += precio
    print(nombre,'su monto a cancelar es \n', acumulado)
    c = input('Ingrese si para volver a facturar \n')
print('Programa terminado')

