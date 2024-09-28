# Escribe un programa que tome un número entero y calcule la suma de sus dígitos.

palabra = (input("Ingresa un número entero: "))
#suma = sum(int(caracteres) for caracteres in palabra)
suma=0
for caracteres in palabra:
    num = int(caracteres)
    suma+=num
print("La suma de los dígitos es:", suma)
