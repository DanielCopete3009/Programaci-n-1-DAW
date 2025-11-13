def compara_arrays(lista1, lista2, lista3):
    # Primero, comparo las longitudes de las tres listas
    if len(lista1) != len(lista2) and  len(lista3):
        return False
    
    # Recorro las tres listas
    for i in range(len(lista1)):
        # Comparo los elementos sin tener en cuenta las mayúsculas/minúsculas
        if lista1[i].lower() != lista2[i].lower() or lista2[i].lower() != lista3[i].lower():
            return False
    
   
    return True

a = ["h","o","l","a"]
b = ["H","o","l","a"]
c = ["H","O","L","A"]

print(compara_arrays(a,b,c))
