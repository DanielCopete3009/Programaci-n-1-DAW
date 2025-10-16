nombre = input("introduce un nombre:")
clave = input("Introduzca una clave:")
longitud = len(clave)
while (len(clave) < 8):
    print("la contraseña debe tener al menos 8 caracteres")
    clave = input("introduce una clave de al menos 8 caracteres:")

print("contraseña correcta,","bienvenido", nombre,"!")
    
