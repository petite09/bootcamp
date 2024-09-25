# Escribe un programa que tome un número entero y calcule la suma de sus dígitos.

num = (input("Ingresa un número entero: "))
suma = sum(int(digito) for digito in num)
print("La suma de los dígitos es:", suma)

#No entiendo en qué parte se define digito 
