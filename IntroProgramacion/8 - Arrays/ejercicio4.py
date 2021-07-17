arrayDado = [109, 13, 10, 76, 155, 76, 98, 36]

maxValor = arrayDado[0]
minValor = arrayDado[0]

for elemento in arrayDado:
    if elemento > maxValor:
        maxValor = elemento
    if elemento < minValor:
        minValor = elemento

print(f'El valor maximo es:\t{maxValor}')
print(f'El valor minimo es:\t{minValor}')