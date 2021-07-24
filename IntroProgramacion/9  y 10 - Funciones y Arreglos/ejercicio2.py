import sys
import copy

def generadorListaMayoresVeinte():
    tempArrayMayores20 = []
    tempArrayResto = []

    for operacion in range(15):
        tempNumero = int(input(f'Numero #{operacion+1} - Por favor introduzca un numero >'))
        if tempNumero > 20:
            tempArrayMayores20.append(tempNumero)
        else:
            tempArrayResto.append(tempNumero)

    return tempArrayMayores20, tempArrayResto
    
def chequearArrayMayores20(array):
    tempArray = copy.deepcopy(array)
    cantidadNumeros = len(tempArray)

    if cantidadNumeros > 8:
        tempArray = tempArray[0:8]
    elif 8 > cantidadNumeros > 0:
        for operacion in range(8 - cantidadNumeros):
            tempArray.append(tempArray[cantidadNumeros-1])
    elif cantidadNumeros == 0:
        print("No hay numeros mayores a 20 en el array!")
        sys.exit(1)
    
    return tempArray

def promedioArray(array):
    tempArray = copy.deepcopy(array)
    sumaElementos = 0
    for elemento in tempArray:
        sumaElementos += elemento
    promedioElementos = sumaElementos / len(array)

    return promedioElementos

def buscadorMaximo(array):
    tempMax = array[0]
    for elemento in array:
        if elemento > tempMax:
            tempMax = elemento
    
    return tempMax

def buscadorIndice(valor, array):
    tempArray = copy.deepcopy(array)
    i = 0
    for elemento in tempArray:
        if valor == elemento:
            break
        i += 1
    return i

def multiplicarIndicesPares(array):
    tempArray = copy.deepcopy(array)
    resultadoMult = 1
    cantidadNumeros = len(array)

    for indice in range(0, cantidadNumeros, 2):
        resultadoMult *= tempArray[indice]

    return resultadoMult

if __name__ == '__main__':
    arrayMayores20, arrayResto = generadorListaMayoresVeinte()

    arrayMayores20 = chequearArrayMayores20(arrayMayores20)
    print(arrayMayores20)

    promedioResto = promedioArray(arrayResto)
    print(promedioResto)

    maximoElemento = buscadorMaximo(arrayMayores20)
    indiceMaximo = buscadorIndice(maximoElemento, arrayMayores20)
    if indiceMaximo == 0:
        print(arrayMayores20[0])
    else:
        print(arrayMayores20[indiceMaximo - 1])

    factorialIndicesPares = multiplicarIndicesPares(arrayMayores20)
    print(factorialIndicesPares)
