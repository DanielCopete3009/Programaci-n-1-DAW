#Tipos de triangulo

ladoa = int(input("introduzca distancia lado a en cm:"))
ladob = int(input("introduzca distancia lado b en cm:"))
ladoc = int(input("introduzca distancia lado c en cm:"))
if ladoa + ladob > c and ladoa + ladoc > ladob and ladob + ladoc > ladoa:
        if ladoa == ladob ==ladoc :
        print("el triangulo es equilatero")
        elif ladoa == ladob or ladob == ladoc or ladoa == ladoc:
        print("el triangulo es isósceles")
        else :
        print("el triangulo es escaleno")
else:
        print("los lados no pueden formar un triangulo")
