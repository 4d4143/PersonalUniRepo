arrayEjercicio = [23, 51, 22, 53, 5, 43, 63, 78, 99, 15]

print(arrayEjercicio[3]) #imprimir cuarto componente

for componente in arrayEjercicio[::-1]:
    print(componente) #imprimir array en reversa

print(arrayEjercicio[0] * arrayEjercicio[-1]) #imprimir multiplicacion entre primer y ultimo elemento

for indice in range(0, len(arrayEjercicio)):
    if indice % 2 == 1:
        print(arrayEjercicio[indice]) #Imprime componentes impares

sumaComponentesIndicePar = 0
for indice in range(0, len(arrayEjercicio)):
    if indice % 2 == 0:
        sumaComponentesIndicePar += arrayEjercicio[indice] #Sumo componentes con indice par
print(sumaComponentesIndicePar)

multiplicacionComponentesIndiceImpar = 1
for indice in range(0, len(arrayEjercicio)):
    if indice % 2 == 1:
        multiplicacionComponentesIndiceImpar *= arrayEjercicio[indice] #Multiplico componentes con indice impar
print(multiplicacionComponentesIndiceImpar)

aux = arrayEjercicio[0]
arrayEjercicio[0] = arrayEjercicio[-1]
arrayEjercicio[-1] = aux

print(arrayEjercicio) #Intercambio primer y ultimo elemento