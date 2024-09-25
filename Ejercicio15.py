# Escribe un programa que imprima la tabla de multiplicar del 1 al 10 para un número dado por el usuario.

num = int(input("Ingresa un número: "))
for i in range (1,11): #No incluye el 11, llega hasta el 10
    print(f"{num} x {i} = {num * i}")