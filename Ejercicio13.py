#Escribe un programa que calcule el factorial de un número.

def calcular_factorial(n):
    factorial = 1 #se inicializa el factorial en 1, porque 0! = 1 por definición. Recordar que el factorial es solo para números positivos.
    for i in range(1, n+1):
        factorial *= i
        
    return factorial

numero = int(input("Introduce un número: "))

#Solicitud al usuario

resultado = calcular_factorial(numero)

#Se puede agregar un paso para verificar que el número ingresado sea positivo y visualización de resultado

if numero < 0:
    print(f"El factorial no está definido para números negativos.")
else:
    print(f"El factorial de {numero} es {resultado}")
