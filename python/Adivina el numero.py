# Hola como estan?
import random

# Genera un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

# Solicita la entrada del jugador
intentos = 0
adivinado = False
while not adivinado:
    suposicion = input("Adivina el número (entre 1 y 100): ")
    suposicion = int(suposicion)
    intentos += 1

    # Compara la suposición del jugador con el número secreto
    if suposicion == numero_secreto:
        adivinado = True
        print("¡Acertaste! El número secreto era", numero_secreto)
    else:
        if suposicion < numero_secreto:
            print("Tu suposición es demasiado baja.")
        else:
            print("Tu suposición es demasiado alta.")

# Imprime el número de intentos realizados
print("Hiciste", intentos, "intentos.")
