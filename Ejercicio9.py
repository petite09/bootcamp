#Escribe un programa que solicite tres numeros y determine cuál es el mayor.

#Definimos la función. Se comparan tres números y devuelve el mayor.

def encontrar_mayor(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

#Primera condición, se verifica el primer número.
#Segunda condición: si no se cumple la primera, se verifica el num2.
#Caso restante, si ninguna de las dos condiciones anteriores se cumple, entonces el número mayor será num3.

#Solicitamos números al usuario

numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
numero3 = float(input("Introduce el tercer número: "))

#Uso de la función y se muestra el resultado
mayor = encontrar_mayor(numero1, numero2, numero3) #en la variable mayor, "llamamos" a la función encontrar_mayor, definida previamente, y la aplicamos a los números ingresados por el usuario.
print("El número mayor es: ", mayor)