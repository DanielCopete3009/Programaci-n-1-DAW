cantidad=int(input("introduce la cantidad: "))

numeros= [0] * cantidad

i=0

while i < cantidad:
    numeros[i]=int(input("introduce el numero: "))
    i +=1

print("Los numeros en orden inverso son :")
i=cantidad-1
while i >=0:
    print(numeros[i])
    i-=1

print("la lista es:",numeros)
