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

if __name__ == '__main__':
    arrayEjercicio = generadorListaPosNeg()
    print(arrayEjercicio)