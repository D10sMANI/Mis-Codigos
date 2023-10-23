#if con else

#ejercicio: calcular promedio

print("vamos a calcular tu promedio para ver si aprobaste el curso")
nombre = input("cual es tu nombre? ")
math = int(input(nombre + ",Cual es tu nota en matematicas?"))
quimica = int(input(nombre + ",Cual es tu nota en quimica?"))
bio = int(input(nombre + ",Cual es tu nota en biologia?"))
resultado = (math + quimica + bio) / 3
if resultado >= 7:
    print('Felicidades, "aprobaste" el curso con ', round(resultado,2))
else:
    print('tristemente "no aprobaste" el curso con ', round(resultado,2))
print("fin")   