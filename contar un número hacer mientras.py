# Pedir al usuario un número entero positivo
numero = int(input("Introduce un número entero positivo: "))

i= 1

while True:
    if i <= numero:
        print(i,end=",")
        i +=1
    
    else :
     print("fin")
     break

