suma = 0
numero = int(input("Ingresa un número (0 para terminar): "))
# Iniciamos el bucle donde seguimos pidiendo números hasta que el usuario ingrese 0
while True:
    suma += numero
    if numero == 0:
        break


print("La suma total es:", suma)


