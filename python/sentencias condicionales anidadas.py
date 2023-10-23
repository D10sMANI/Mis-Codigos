# Tener una instruccion condicional dentro de otra

print("Conversor \n")

print("Menu de opciones:\n")

print("presione 1 para convertir de numero a palabra")
print("Presione 2 para convertir de palabra a numero \n")

opcion = int(input("Cual es tu opcion? \n"))

if opcion == 1:
    print("\n Conversor de numero a palabra \n")
    
    opcion_uno = int(input("Que numero quieres convertir a palabra?"))
    if opcion_uno == 1:
        print('El numero es "UNO"')
    elif opcion_uno == 2:
        print('El numero es "DOS"')
    elif opcion_uno == 3:
        print('El numero es "TRES"')
    elif opcion_uno == 4:
        print('El numero es "CUATRO"')
    elif opcion_uno == 5:
        print('EL numero es "CINCO"')
    else:
        print("Opcion no disponible")
elif opcion ==2:
    print("\n conversor de palabra a numero \n")
    opcion_dos = input("Que palabra quieres convertir a numero?")
    if opcion_dos == 'uno':
        print('El numero es "1"')
    elif opcion_dos == 'dos':
        print('El numero es "2"')
    elif opcion_dos == 'tres':
        print('El numero es "3"')
    elif opcion_dos == 'cuatro':
        print('El numero es "4"')
    elif opcion_dos == 'cinco':
        print('EL numero es "5"')
    else:
        print("Opcion no disponible")
else :
    print ("Opcion no valida")
print('FIN')
