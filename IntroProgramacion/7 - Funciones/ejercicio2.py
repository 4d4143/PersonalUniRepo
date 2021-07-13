#construir una funcion que permita devolver la potencia de un numero ingresando su numero y exponente

#implementacion naive

def potenciaNumero(n, e):
    resultado = n
    exponente = e
    if e == 0:
        resultado = 1
    else:
        while exponente > 1:
            resultado *= n
            exponente -= 1

    return resultado

print("Resultado de 10 al cuadrado:\t", potenciaNumero(10, 2)) # deberia dar 100

    