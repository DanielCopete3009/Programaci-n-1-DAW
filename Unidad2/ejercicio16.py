def Busqueda_binaria(array, n):
    inicio = 0
    fin = len(array) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        
        if array[medio] == n:
            return medio
        elif array[medio] < n:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1

# 
# array_utilizada = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
# num_buscar = int(input("Introduce cualquier decena del 0-90: "))
# 
# # Llamada a la función
# indice = Busqueda_binaria(array_utilizada, num_buscar)
# 
# if indice != -1:
#     print("El número", num_buscar, "se encuentra en el índice", indice)
# else:
#     print("El número", num_buscar, "no se encuentra en el array.")

        