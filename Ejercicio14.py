# Escribe un programa que imprima todos los números pares de una lista dada.

def imprimir_pares(lista_numeros):
    for numero in lista_numeros:
        if numero % 2 == 0:
            print(numero)

#Lista

lista = [1, 2, 3, 4, 5 ,6 ,7, 8, 9, 10]

imprimir_pares(lista)


#otra opción es:
numeros = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
pares = [num for num in numeros if num %2 == 0]
print("Los números pares en la lista son:", pares)