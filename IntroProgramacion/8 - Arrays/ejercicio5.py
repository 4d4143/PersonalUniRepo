arrayDado = [109, 13, 10, 76, 155, 76, 98, 36, 10, 10]

#Dado un array, imprimir el lugar que ocupa el minimo. Si se repite. imprimir todos los
#indices donde se repite

#Primer buscar valor minimo. Despues almacenar indices donde aparece.

minValor = arrayDado[0]
posicionesMinValor = []

for elemento in arrayDado:
    if elemento < minValor:
        minValor = elemento

for indice, elemento in enumerate(arrayDado):
    print(f'Elemento:{elemento}\tIndice:{indice}')
    if elemento == minValor:
        posicionesMinValor.append(indice)

print(posicionesMinValor)
