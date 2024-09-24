#Escribe un programa que que solicite un número al usuario e indique si es par o impar
numero = int(input("numero "))
division = numero%2

if division == 0:
    print("Numero par")
else:
    print ("Numero impar")