def suma (x,y):
    suma = x+y
    print("la sumatoria de los valores es: \n", suma)

def resta (x,y):
    resta = x-y
    print("la resta de los valores es: \n", resta)

def multiplicacion (x,y):
    multiplicacion = x*y
    print("la multiplicacion de los valores es: \n", multiplicacion)

def division (x,y):
    division = x/y
    print("la division de los valores es: \n", division)
x = int(input("Ingrese el valor del primer numero "))
y = int(input("Ingrese el valor del segundo numero "))

print("MENU \n""1 = Suma \n" "2 = Resta \n" "3 = Multiplicacion \n" "4 = division \n")
o = int(input("Elige la operacion a realizar \n"))

if (o == 1):
    suma(x,y)
elif (o == 2):
    resta(x,y)
elif (o == 3):
    multiplicacion(x,y)
elif (o == 4):
    division(x,y)
else :
    print("Opción no valida")
    