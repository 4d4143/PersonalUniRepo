def cargarMultiplosCinco(arrayObjetivo):
    banderaCero = False
    while banderaCero == False:
        tempNumero = int(input("Por favor, introduzca un numero (0 para salir) > "))
        if tempNumero == 0:
            banderaCero = True
        else:
            if tempNumero % 5 == 0:
                arrayObjetivo.append(tempNumero)

def mostrarTresMayores(arrayFuente):
    if len(arrayFuente) > 2:
        tempArray = []
        primerMax = helperPrimerMax(arrayFuente)
        segundoMax = helperSegundoMax(arrayFuente, primerMax)
        tercerMax = helperTercerMax(arrayFuente, primerMax, segundoMax)
        tempArray.append(primerMax)
        tempArray.append(segundoMax)
        tempArray.append(tercerMax)

        print(tempArray)
    else:
        print("El array introducido no tiene 3 o mas valores!")

def helperPrimerMax(arrayFuente):
    tempArray = [elemento for elemento in arrayFuente]
    primerMax = tempArray[0]
    for elemento in tempArray:
        if elemento > primerMax:
            primerMax = elemento
    
    return primerMax

def helperSegundoMax(arrayFuente, primerMax):
    tempArray = [elemento for elemento in arrayFuente]
    segundoMax = tempArray[0]
    for elemento in tempArray:
        if elemento > segundoMax and elemento != primerMax:
            segundoMax = elemento
    return segundoMax

def helperTercerMax(arrayFuente, primerMax, segundoMax):
    tempArray = [elemento for elemento in arrayFuente]
    tercerMax = tempArray[0]
    for elemento in tempArray:
        if elemento > tercerMax and elemento != primerMax and elemento != segundoMax:
            tercerMax = elemento
    return tercerMax

def mostrarMultiplosDiez(arrayFuente):
    tempArray = []
    for elemento in arrayFuente:
        if elemento % 10 == 0:
            tempArray.append(elemento)
    if len(tempArray) > 0:
        print(tempArray)
    else:
        print("No hay multiplos de 10 entre los valores introducidos!")

def helperContarElemento(arrayObjetivo, elementoObjetivo):
    resultadoContador = 0
    for elemento in arrayObjetivo:
        if elemento == elementoObjetivo:
            resultadoContador += 1
    return resultadoContador

def eliminadorValoresMinimos(arrayObjetivo):
    if len(arrayObjetivo) > 0:
        valorMinimo = arrayObjetivo[0]
        for elemento in arrayObjetivo:
            if elemento < valorMinimo:
                valorMinimo = elemento
        contadorValorMinimo = helperContarElemento(arrayObjetivo, valorMinimo)
        while contadorValorMinimo > 0:
            arrayObjetivo.remove(valorMinimo)
            contadorValorMinimo -= 1
    else:
        print("El arreglo introducido no tiene elementos!")

arrayEjercicio = []
cargarMultiplosCinco(arrayEjercicio)
print("Los multiplos de 5 ingresados son:")
print(arrayEjercicio)

print("\nDe esos multiplos de 5, los tres mayores numeros ingresados son:")
mostrarTresMayores(arrayEjercicio)

print("\nDe esos multiplos de 5, los siguientes numeros son tambien multiplos de 10:")
mostrarMultiplosDiez(arrayEjercicio)

print("\nSi dentro de esos multiplos de 5 eliminamos al valor minimo, se veria asi:")
eliminadorValoresMinimos(arrayEjercicio)
print(arrayEjercicio)


