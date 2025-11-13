import ejercicio16
import ejercicio15


numeros = [55,10,20,00,4,500,60,70,80,30]
print(f"Dado el array desordenado: {numeros}")
eleccion = 60

print("Búsqueda Lineal")
resultado=ejercicio15.busquedaLineal(numeros, eleccion)
if resultado != -1:
    print("El numero",eleccion,"se encuentra en la posicion",(resultado))
else:
    print("Ese numero no se encuentra.")
    
print("Búsqueda Binaria")
resultado=ejercicio16.Busqueda_binaria(numeros, eleccion)
if resultado != -1:
    print("El numero",eleccion,"se encuentra en la posicion",(resultado))
else:
    print("Ese numero no se encuentra.")

numeros = [0,10,20,30,40,50,60,70,80,90]
print(f"Mientras que dado un array sí ordenado{numeros}")

print("Búsqueda Lineal")
resultado=ejercicio15.busquedaLineal(numeros, eleccion)
if resultado != -1:
    print("El numero",eleccion,"se encuentra en la posicion",(resultado))
else:
    print("Ese numero no se encuentra.")
    
print("Búsqueda Binaria")
resultado=ejercicio16.Busqueda_binaria(numeros, eleccion)
if resultado != -1:
    print("El numero",eleccion,"se encuentra en la posicion",(resultado))
else:
    print("Ese numero no se encuentra.")