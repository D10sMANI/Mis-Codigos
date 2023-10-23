# Mas optimo que el while

# Contador = 1
#print(Contador)
#while contador < 1000 :
#   contador += 1 
#    print(contador)

for contador in range(1000):
    print(contador)


# Otro uso

def run() :
    nombre = input('Escribe tu nombre: \n')
    for letra in nombre :
        print(letra)
if __name__ == '__main__' :
    run()
