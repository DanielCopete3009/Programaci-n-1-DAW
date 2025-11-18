matriz = [
    ["A", "B", "C"],
    ["D", "E", "F"],
    ["G", "H", "I"]
]

# 
# i = 0
# while i < len(matriz[0]):  
#     j = 0
#     while j < len(matriz):  
#         print(matriz[j][i], end=' ')  
#         j += 1
#     i += 1
#
# for i in range(len(matriz[0])):  
#     
#     for j in range(len(matriz)):    
#         print(matriz[j][i], end=' ')


for columna in matriz:
   
    for elemento in columna:
        print(elemento, end=' ')



