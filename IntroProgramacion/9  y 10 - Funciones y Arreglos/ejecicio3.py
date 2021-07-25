def generadorListaPosNeg():
    tempArray = []

    for operacion in range(5):
        tempNumeroPos = int(input(f'Por favor introduzca el numero positivo {operacion + 1} de 5 -> '))
        while tempNumeroPos < 0:
            tempNumeroPos = int(input(f'Por favor introduzca el numero positivo {operacion + 1} de 5 -> '))
        tempArray.append(tempNumeroPos)

    for operacion in range(5):
        tempNumeroNeg = int(input(f'Por favor introduzca el numero negativo {operacion + 1} de 5 -> '))
        while tempNumeroNeg > 0:
            tempNumeroNeg = int(input(f'Por favor introduzca el numero negativo {operacion + 1} de 5 -> '))
        tempArray.append(tempNumeroNeg)

    return tempArray

def promedioArray(array):
    tempArray = array
    sumaElementos = 0
    for elemento in tempArray:
        sumaElementos += elemento
    promedioElementos = sumaElementos / len(array)

    return promedioElementos

def generadorMultiplosCuatro(arrayFuente):
    arrayTemp = []
    for elemento in arrayFuente:
        if elemento % 4 == 0:
            arrayTemp.append(elemento)

    return arrayTemp

def mostrarMultiplosTres(arrayFuente):
    tempArray = []
    for elemento in arrayFuente:
        if elemento % 3 == 0:
            tempArray.append(elemento)

    if tempArray:
        print(tempArray)
    else:
        print("No hay multiplos de 3 entre los multiplos de 4!")

if __name__ == '__main__':
    arrayEjercicio = generadorListaPosNeg()
    print(arrayEjercicio)

    arrayNegativos = arrayEjercicio[5:]
    print(promedioArray(arrayNegativos))

    arrayEjercicio.sort()
    print(arrayEjercicio)

    arrayMultiplosCuatro = generadorMultiplosCuatro(arrayEjercicio)
    if arrayMultiplosCuatro:
        print(arrayMultiplosCuatro)
        mostrarMultiplosTres(arrayMultiplosCuatro)
    else:
        print("No hay multiplos de cuatro entre los numeros introducidos!")
 
