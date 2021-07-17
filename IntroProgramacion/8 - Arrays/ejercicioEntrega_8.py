arrayEjercicio = []

#Cargamos doce numeros enteros
for iteracion in range(12): 
    numeroInput = int(input(f'Numero #{iteracion + 1} - Por favor ingrese un numero >'))
    arrayEjercicio.append(numeroInput)

#Una vez cargado, mostrarlo
print("\nLos numeros cargados son los siguientes:")
print(arrayEjercicio)

#Elemento minimo y elemento maximo
maxValor = arrayEjercicio[0]
minValor = arrayEjercicio[0]

for elemento in arrayEjercicio:
    if elemento > maxValor:
        maxValor = elemento
    if elemento < minValor:
        minValor = elemento

#Ubico los indices de max y min 
posicionMaxValor = arrayEjercicio.index(maxValor)
posicionMinValor = arrayEjercicio.index(minValor)

#muestro cuales son y sus indices
print(f'\nEl valor maximo es {maxValor} y su indice en el array es {posicionMaxValor}')
print(f'El valor minimo es {minValor} y su indice en el array es {posicionMinValor}')

#calculamos el promedio de los valores ubicados en indices pares (0, 2, 4,...)
sumaValoresIndicePar = 0
for indice in range(0, 12, 2):
    sumaValoresIndicePar += arrayEjercicio[indice]
promedioIndicePar = sumaValoresIndicePar / 7 #Son 7 indices pares. Hay que contar al 0.
print(f'\nEl promedio de los valores en indices pares es:{promedioIndicePar}')

#Insertamos la mitad del elemento maximo despues de este
arrayEjercicio.insert(posicionMaxValor + 1, maxValor / 2)
print("\nArray con valor nuevo insertado: ")
print(arrayEjercicio)

#hacemos Sort con parametro reverse=True
arrayEjercicio.sort(reverse=True)
print("\nArray con valores ordenados mayor a menor")
print(arrayEjercicio)












