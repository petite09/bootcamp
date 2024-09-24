#Escribe un programa que cuente cuántas vocales hay en una cadena dada.

def contar_vocales(cadena):
    vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
    contador = 0
    
    for letra in cadena:
        if letra in vocales:
            contador +=1
    
    return contador

cadena = input("Ingresa tu cadena: ")
print ("El número de vocales es:", contar_vocales(cadena))