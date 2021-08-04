def cargarArray(arrayObjetivo):
    #Creo dos variables para trackear la cantidad de nums pos y negs
    numerosPositivos = 0
    numerosNegativos = 0

    #El tamaño maximo del array debe ser 12. 6 nums pos + 6 nums negs
    numeroInput = int(input("Por favor 6 numeros positivos y 6 negativos. Ingrese 0 para terminar > "))
    while len(arrayObjetivo) < 12 and numeroInput != 0:

        if numeroInput > 0 and numerosPositivos < 6:
            numerosPositivos += 1
            arrayObjetivo.append(numeroInput)
        elif numeroInput < 0 and numerosNegativos < 6:
            numerosNegativos += 1
            arrayObjetivo.append(numeroInput)

        numeroInput = int(input("Por favor 6 numeros positivos y 6 negativos. Ingrese 0 para terminar > "))

def agregarConsecutivoPares(arrayObjetivo):
    for elemento in arrayObjetivo:
        if elemento % 2 == 0:
            arrayObjetivo.append(elemento + 1)

def hallarMaxPos(arrayFuente, indicePrimerPos):
    maxPos = arrayFuente[indicePrimerPos]
    for elemento in arrayFuente:
        if elemento > maxPos and elemento > 0:
            maxPos = elemento

    return maxPos

#Que pasa si JUSTO el primer valor introducido por el usuario fue
def hallarMinPos(arrayFuente, indicePrimerPos):
    minPos = arrayFuente[indicePrimerPos]
    if minPos < 0:
        minPos *= -1
    for elemento in arrayFuente:
        if elemento < minPos and elemento > 0:
            minPos = elemento
    
    return minPos

def hallarPositivos(arrayFuente):
    indicePrimerPos = []
    for indice in range(len(arrayFuente)):
        if arrayFuente[indice] > 0:
            indicePrimerPos.append(indice)

    return indicePrimerPos

def generarMultiplosTres(arrayFuente):
    arrayNuevo = []
    for elemento in arrayFuente:
        if elemento % 3 == 0:
            arrayNuevo.append(elemento)

    return arrayNuevo

def mostrarArray(arrayFuente):
    for elemento in arrayFuente:
        print(elemento, end=" ")
    print("\n")

if __name__ == '__main__':
    arrayEjercicio = []
    cargarArray(arrayEjercicio)
    print("Los valores cargados fueron:")
    mostrarArray(arrayEjercicio)

    if len(arrayEjercicio) > 0:
        #agregar el consecutivo de cada par si es que los hay
        agregarConsecutivoPares(arrayEjercicio)
        print("Despues de agregar los consecutivos de los pares (Si es lo que habia), los valores son:")
        mostrarArray(arrayEjercicio)

        #calcular el mayor positivo y el menor positivo
        indicesPositivos = hallarPositivos(arrayEjercicio)
        if indicesPositivos:
            minPos = hallarMinPos(arrayEjercicio, indicesPositivos[0])
            maxPos = hallarMaxPos(arrayEjercicio, indicesPositivos[0])
            print(f'El minimo positivo hallado fue: {minPos}')
            print(f'El maximo positivo hallado fue: {maxPos}')

        #generar otro arreglo con los multiplos de 3
        arrayMultiplosTres = generarMultiplosTres(arrayEjercicio)
        if arrayMultiplosTres:
            print("Los multiplos de 3 encontrados entre los valores introducidos fueron:")
            mostrarArray(arrayMultiplosTres)
    else:
        print("No se cargaron valores al arreglo!")