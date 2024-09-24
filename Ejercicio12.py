#Escribe un programa donde el usuario tenga que adivinar un número entre 1 y 10.

import random
numero_secreto = random.randint(1,10)
adivinanza = int(input("Adivina un número entre 1 y 10: "))
if adivinanza == numero_secreto:
    print("¡Felicidades! Adivinaste el número secreto")
else:
    print(f"No adivinaste. El número secreto era {numero_secreto}.")

# Primero es necesario importar el módulo (fichero .py que alberga un conjunto de funciones, variables, clases o constantes).
# Se define variable numero_secreto igual al módulo que en este caso es random: Sirve para generar números aleatorios.
# randint() es una función que permite obetner un número entero dentro de un rango especificado, en este caso 1 y 10.
# Se crea otra variable = adivinanza, que corresponde al input, lo que ingresa el usuario.
# se definen las condiciones.
