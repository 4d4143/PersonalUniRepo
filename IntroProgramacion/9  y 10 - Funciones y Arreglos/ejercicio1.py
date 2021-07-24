def cargarNumerosPares(cantidad):
    tempArray = []
    for instancia in range(cantidad):
        tempNumero = int(input(f'Numero {instancia + 1} - Por favor cargue un numero par'))
        while tempNumero % 2 != 0:
            print("El valor introducido no es un numero par!")
            tempNumero = int(input(f'Numero {instancia + 1} - Por favor cargue un numero par'))
        tempArray.append(tempNumero)

    
    return tempArray

def cargarNumerosMult5(cantidad):
    tempArray = []
    for instancia in range(cantidad):
        tempNumero = int(input(f'Numero {instancia + 1} - Por favor cargue un numero multiplo de 5'))
        while tempNumero % 5 != 0:
            print("El valor introducido no es un multiplo de 5!")
            tempNumero = int(input(f'Numero {instancia + 1} - Por favor cargue un numero multiplo de 5'))
        tempArray.append(tempNumero)
    
    return tempArray

def sumaArrays(arrayA, arrayB):
    tempArray = []

    if len(arrayA) == len(arrayB):
        for indice in range(len(arrayA)):
            tempArray.append(arrayA[indice] + arrayB[indice])

    return tempArray

def unionArrays(arrayA, arrayB):
    tempArray = []
    for elemento in arrayA:
        tempArray.append(elemento)
    
    for elemento in arrayB:
        tempArray.append(elemento)

    return tempArray

def invertirArray(array):
    tempArray = array[::-1]
    return tempArray

def buscadorMaximo(array):
    tempMax = array[0]
    for elemento in array:
        if elemento > tempMax:
            tempMax = elemento
    
    return tempMax

def buscadorIndices(valor, array):
    tempPosiciones = []
    indice = 0
    for elemento in array:
        if elemento == valor:
            tempPosiciones.append(indice)
        indice += 1
    
    return tempPosiciones

def seteadorCeros(array, indice):
    tempArray = array
    ultimoIndice = len(array) - 1
    if indice >= ultimoIndice:
        print("El indice introducido es el ultimo! No hay valores a su derecha")
        return tempArray

    elif indice < 0:
        print("El indice no puede ser negativo!")
        return tempArray

    else:
        for indiceTemp in range(indice+1, ultimoIndice+1):
            tempArray[indiceTemp] = 0
        return tempArray

def promedioArray(array):
    tempArray = array
    sumaElementos = 0
    for elemento in tempArray:
        sumaElementos += elemento
    promedioElementos = sumaElementos / len(array)

    return promedioElementos

def contadorMayoresValor(array, valor):
    tempArray = array
    contador = 0
    for elemento in array:
        if elemento > valor:
            contador += 1
    return contador



if __name__ == '__main__':
    array_A = cargarNumerosPares(10)
    print(array_A)

    array_B = cargarNumerosMult5(10)
    print(array_B)

    array_C = sumaArrays(array_A, array_B)
    print(array_C)

    array_D = unionArrays(array_A, array_B)
    print(array_D)

    print(invertirArray(array_A))
    indices_maximo_B = buscadorIndices(buscadorMaximo(array_B), array_B)
    print(seteadorCeros(array_B, indices_maximo_B[-1]))

    print(promedioArray(array_C))

    print(contadorMayoresValor(array_C, promedioArray(array_C)))