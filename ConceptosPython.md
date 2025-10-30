Conceptos básicos de Python

Python es un lenguaje de programación muy popular por su sencillez y legibilidad. Se utiliza en muchos campos como la inteligencia artificial, el desarrollo web, la automatización, la ciencia de datos y la educación. A continuación se explican algunos de sus conceptos fundamentales:

1. Sintaxis básica

Python utiliza una sintaxis clara y fácil de entender. A diferencia de otros lenguajes, no se usan llaves {} para definir bloques de código, sino la indentación (sangría). Por ejemplo:

if 5 > 3:
    print("Cinco es mayor que tres")


El uso correcto de espacios es esencial, ya que indica qué líneas pertenecen a un mismo bloque.

2. Variables y tipos de datos

Las variables se usan para almacenar información. No es necesario indicar el tipo de dato al declararlas:

nombre = "Ana"
edad = 17
altura = 1.75


Los tipos de datos básicos en Python son:

int: números enteros (10, -3)

float: números decimales (3.14, 0.5)

str: cadenas de texto ("Hola")

bool: valores lógicos (True o False)

3. Operadores

Python incluye operadores aritméticos (+, -, *, /, **, %), de comparación (==, !=, >, <, >=, <=) y lógicos (and, or, not).

4. Estructuras de control

Permiten tomar decisiones o repetir acciones:

Condicionales:

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


Bucles:

for: se usa para repetir un número determinado de veces.

for i in range(5):
    print(i)


while: se repite mientras se cumpla una condición.

while edad < 18:
    print("Todavía eres menor")
    edad += 1

5. Funciones

Las funciones permiten reutilizar código. Se definen con la palabra clave def:

def saludar(nombre):
    print("Hola,", nombre)

saludar("Ana")

6. Listas y colecciones

Las listas son estructuras que almacenan varios valores:

frutas = ["manzana", "pera", "naranja"]
print(frutas[0])  # Accede al primer elemento


También existen otros tipos de colecciones como las tuplas, los conjuntos (set) y los diccionarios (dict).

7. Entrada y salida

Para recibir información del usuario se usa input():

nombre = input("¿Cómo te llamas? ")
print("Hola", nombre)

8. Comentarios

Los comentarios sirven para explicar el código y no se ejecutan:

# Esto es un comentario