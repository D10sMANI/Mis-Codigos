# Sistema que determine los dias de vacaciones a los que tiene derecho un trabajador
# Departamento de Atencion al cliente (CLAVE_1); 1año= 6dias, 2 a 6años= 14dias, 7años a mas= 20dias
# Departamento de logistica (CLAVE_2); 1año= 7dias, 2 a 6años= 15dias, 7años a mas= 22dias
# Gerencia (CLAVE_3); 1año= 10dias, 2 a 6años= 20dias, 7años a mas= 30dias
# Solicitar: nombre, clave y antiguedad. Mostrar: nombre y dias de vacaciones
# La empresa se llama "Compañia multinacional RAPPI"

nombre = input("Ingrese su nombre a continuacion...  ")
print("bienvenido ", nombre," al sistema de dias de vacaciones de la Compañia Multinacional RAPPI \n")
clave = int(input('Por favor, ingrese su clave de trabajor... '))
if clave == 1:
    print('Usted trabaja en el departamento de atencion al cliente \n')
elif clave == 2:
    print('Usted trabaja en el departamento de logistica \n')
elif clave == 3:
    print('Uested trabaja en Gerencia \n')
else :
    print('Numero de clave incorrecto')
tiempo = int(input('Ingrese su antiguedad en años... '))
if clave ==1 :
    if tiempo < 2 and tiempo >=1 :
        print(nombre, ' tiene derecho a 6 dias de vacaciones \n')
    if tiempo >= 2 and tiempo < 7 :
        print(nombre, ' tiene derecho a 14 dias de vacaciones \n')
    if tiempo >= 7 :
        print(nombre, ' tiene derecho a 20 dias de vacaciones \n')
elif clave ==2 :
    if tiempo < 2 and tiempo >=1 :
        print(nombre, ' tiene derecho a 7 dias de vacaciones \n')
    if tiempo >= 2 and tiempo < 7 :
        print(nombre, ' tiene derecho a 15 dias de vacaciones \n')
    if tiempo >= 7 :
        print('Usted tiene derecho a 22 dias de vacaciones \n')
elif clave ==3 :
    if tiempo < 2 and tiempo >=1 :
        print(nombre, ' tiene derecho a 10 dias de vacaciones \n')
    if tiempo >= 2 and tiempo < 7 :
        print(nombre, ' tiene derecho a 20 dias de vacaciones \n')
    if tiempo >= 7 :
        print(nombre, ' tiene derecho a 30 dias de vacaciones \n')
else :
    print('Algo salio mal, pro favor intentelo de nuevo')
print('FIN')    