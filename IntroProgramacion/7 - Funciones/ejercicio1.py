#Construir una funcion que devuelva el valor absoluto de un numero ingresado por teclado

def valorAbsoluto():
    inputValue = int(input("Introduzca un numero:\t>"))
    if inputValue >= 0:
        retValue = inputValue
    else:
        retValue = inputValue * -1
    
    return retValue

numeroTest = valorAbsoluto()
print(numeroTest)