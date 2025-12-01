num1 = int(input("Introduce un número: "))

def primo(num):
    if num <= 1:  # Los números menores o iguales a 1 no son primos
        return False
    
    # Comprobamos divisibilidad desde 2 hasta la raíz cuadrada del número
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    
    return True

def primos_hasta(n):
    primos = []  # Lista para guardar los números primos encontrados
    
    for i in range(2, n + 1):
        if primo(i):  # Usamos la función primo() para comprobar
            primos.append(i)
    
    print(f"Números primos hasta {n}: {primos}")
    print(f"Cantidad de números primos encontrados: {len(primos)}")

# Llamamos a la nueva función
primos_hasta(num1)
