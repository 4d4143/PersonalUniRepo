#Se ingresan n numeros. Diseniar un programa que usando una funcion, muestre la mitad de aquellos
#que sean pares

def mostrarMitadPares(numero):
    if numero % 2 == 0:
        print("La mitad de este numero par es:", numero / 2)

cantidadNumeros = int(input("Por favor introduzca la cantidad de numeros a procesar:\t>"))

for iteracion in range(cantidadNumeros):
    numero = int(input("Por favor introduzca un numero:\t>"))
    mostrarMitadPares(numero)
