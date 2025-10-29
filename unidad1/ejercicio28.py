num1 = int(input("Introduce el numero al que se le  va a sumar solo números pares del 0 al 100:"))
total = num1
for i in range(0,100,2):
        total +=i

print("el resultado es:",total)
