#include <stdio.h>
#include <stdlib.h>

int main()
{
    char nombre [] = "Manuel";
    int edad = 20;
    int edad_siguiente = edad + 1;
    printf("Me llamo %s y tengo %d \n", nombre, edad);
    printf("Tengo %d y me llamo %s \n", edad, nombre);
    printf("El proximo a'o tendre %d \n",edad_siguiente);
    return 0;
}
