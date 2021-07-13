def sumaDivisores(numero):
    sumaTotal = 1 #1 siempre es un divisor del numero

    for numeroCandidato in range(2, numero):
        if numero % numeroCandidato == 0:
            sumaTotal += numeroCandidato

    return sumaTotal

def chequearAmistadNumeros(numA, numB, sumDivA, sumDivB):
    if sumDivA == numB and sumDivB == numA:
        print("Los numeros introducidos son amigos.")
    else:
        print("Los numeros introducidos no son amigos.")

if __name__ == '__main__':
    primerNumero = int(input("Por favor introduzca el primer numero\t>"))
    segundoNumero = int(input("Por favor introduzca el segundo numero\t>"))

    sumDivsPrimero = sumaDivisores(primerNumero)
    sumaDivsSegundo = sumaDivisores(segundoNumero)

    chequearAmistadNumeros(primerNumero, segundoNumero, sumDivsPrimero, sumaDivsSegundo)