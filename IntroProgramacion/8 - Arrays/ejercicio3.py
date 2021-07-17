arrayA = [34, 12, 5, 34, 67, 2, 9, 26]
arrayB = [75, 1, 5, 42, 88, 74, 89, 10]
arrayC = [0] * len(arrayA)

for indice in range(0, len(arrayA)):
    arrayC[indice] = arrayA[indice] + arrayB[indice]

print(arrayC)