#asignacion
mensaje = "hola"
mensaje += " "
mensaje += "adios"
print(mensaje)

#concatenacion
mensaje1 = "hola"
mensaje2 = " "
mensaje3 = "como"
mensaje4 = " "
mensaje5 = "estas"
print(mensaje1 + mensaje2 + mensaje3 + mensaje4 + mensaje5)

      
#Busqueda
mensaje = "Hola Manuel"
buscar_subcadena = mensaje.find("Manuel")
print(buscar_subcadena)

#Extracción
mensaje = "Hola Manuel"
extraer_subcadena = mensaje[1:8] #no toma en cuenta el ultimo, en este caso el 8
print(extraer_subcadena)

#comparacion
mensaje_uno = "hola"
mensaje_dos = "hola"
print(mensaje_uno == mensaje_dos)
