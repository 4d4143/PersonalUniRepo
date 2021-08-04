def cargarValores(pesoRetiro, edadRetiro, pesoConstitucion, edadConstitucion):
    print("---CARGANDO VALORES DE ENCUESTA---\n(Introduzca un valor negativo en peso para terminar)\n")

    tempPeso = int(input("Por favor introduzca el peso del encuestado (KG) > "))
    while tempPeso >= 0:
        
        tempEdad = cargarEdad()

        tempEstacion = cargarEstacion()

        if tempEstacion == 1:
            pesoRetiro.append(tempPeso)
            edadRetiro.append(tempEdad)
        elif tempEstacion == 2:
            pesoConstitucion.append(tempPeso)
            edadConstitucion.append(tempEdad)

        tempPeso = int(input("Por favor introduzca el peso del encuestado (KG) > "))

def cargarEdad():
    inputEdad = int(input("Por favor introduzca la edad del encuestado > "))
    while inputEdad < 0:
        print("#### Valor de edad invalido! Debe ser mayor a 0 ####")
        inputEdad = int(input("Por favor introduzca la edad del encuestado > "))
    return inputEdad

def cargarEstacion():
    inputEstacion = int(input("Por favor introduzca el numero de la estacion donde se encuesto\n\
    1-Retiro\n\
    2-Constitucion\n > "))

    while inputEstacion not in [1,2]:
        print("#### Valor de estacion erroneo! Debe ser 1 o 2 ####")
        inputEstacion = int(input("Por favor introduzca el numero de la estacion donde se encuesto\n\
        1-Retiro\n\
        2-Constitucion\n > "))

    return inputEstacion

def mostrarEdadPeso(arrayPeso, arrayEdad, estacion):
    if len(arrayEdad) > 0:
        print(f'Los valores de los encuestados en la estacion {estacion} son:')
        print("Edades:")
        for tempEdad in arrayEdad:
            print(tempEdad, end=" ")
        print()
        print("Pesos:")
        for tempPeso in arrayPeso:
            print(tempPeso, end=" ")
        print()
    else:
        print(f'No hubo encuestados en la estacion {estacion}!\n')

def mostrarResultadoPromedios(resultadoInput):
    print()
    if resultadoInput == "A":
        print("La estacion de Retiro tiene el mayor promedio de peso")
    elif resultadoInput == "B":
        print("La estacion de Constitucion tiene el mayor promedio de peso")
    else:
        print("Ambas estaciones tienen el mismo promedio de peso")
    print()


def compararPromedios(arrayA, arrayB):
    promedioA = promediarArray(arrayA)
    promedioB = promediarArray(arrayB)
    if promedioA > promedioB:
        return "A"
    elif promedioB > promedioA:
        return "B"
    else:
        return "C"

def promediarArray(arrayInput):
    if len(arrayInput) > 0:
        tempCounter = 0
        for elemento in arrayInput:
            tempCounter += elemento
        resultado = tempCounter / len(arrayInput)
        return resultado
    else:
        return 0

if __name__ == '__main__':
    pesoRetiro = []
    edadRetiro = []
    pesoConstitucion = []
    edadConstitucion = []
    cargarValores(pesoRetiro, edadRetiro, pesoConstitucion, edadConstitucion)

    if len(pesoRetiro) > 0 or len(pesoConstitucion) > 0:
        mostrarEdadPeso(pesoRetiro, edadRetiro, "Retiro")
        mostrarEdadPeso(pesoConstitucion, edadConstitucion, "Constitucion")
        
        resultadoCompararPromedios = compararPromedios(pesoRetiro, pesoConstitucion)
        mostrarResultadoPromedios(resultadoCompararPromedios)