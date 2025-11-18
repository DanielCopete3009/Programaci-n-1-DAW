P = [[5,10.5],[8.2,15],[1.5,3]]

suma = 0
for i in range(len(P)):
    for j in range (len(P[0])):
        if j == 1:
            suma += P[i][j]
    
print("la suma es : ",suma)