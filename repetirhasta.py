num = int(input("Introduce un número entero natural:"))

i = 1

while True:
    if i > num:
        break
           
          
    elif i == num:
        print(i)
          
    else:
        print(i,end=",")
    i += 1
