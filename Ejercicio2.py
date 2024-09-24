#Escribe un programa que solicite dos números al usuario y luego imprima la suma

numero1 = input("ingresa un numero ")
numero2 = input("ingresa otro numero ")

numero1 = int(numero1) #El int puede ir antes del input para usar menos lineas de código
numero2 = int(numero2)

suma = numero1 + numero2

print(f"La suma de los números es {suma}")