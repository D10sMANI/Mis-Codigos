# son una instruccion, se ejecutan cuando se establece una condicion logica
# al cumplirse, el programa ejecuta la instruccion asignada a esta condicion

"""
num_uno = 5
if num_uno == 5:
    print("El numero es cinco")
print("fin")
"""

#ejercicio

print("Sistema para calcular el promedio de un alumno")
print("Para que un alunmo apruebe debe tener un promedio mayor que 7")
nombre = input("¿Cual es tu nombre: ")
math = int(input(str(nombre)+ " ¿Cual es tu calificacion en matematicas? "))
quimica = int(input(str(nombre)+ " ¿Cual es tu calificacion en quimica? "))
bio = int(input(str(nombre)+ " ¿Cual es tu calificacion en biologia? "))
promedio =  (math + quimica + bio)/3
promedio = int(promedio)
if promedio >= 7:
    print("Felicidades", nombre,"aprobaste con un promedio de:", promedio)
print("fin")
    
