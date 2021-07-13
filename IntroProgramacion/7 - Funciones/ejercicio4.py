#Diseniar un programa que permita ingresar las dimensiones de un ambiente rectangular y calcular
#superficie del piso
#superficie paredes
#perimetro del ambiente

import math

def superficiePiso(ancho, largo):
    return ancho * largo


def superficieParedes(altura, ancho, largo):
    superficieParedesAncho = altura * ancho * 2
    superficieParedesLargo = altura * largo * 2
    sumaSuperficies = superficieParedesAncho + superficieParedesLargo
    return sumaSuperficies


def perimetroAmbiente(ancho, largo):
    return ancho * 2 + largo * 2


def costoAlfombrar(precioAlfombra, metrosAlfombrar):
    return precioAlfombra * metrosAlfombrar


def costoPintar(precioPintura, areaParedes):
    cantidadLitros = math.ceil(areaParedes / 6)
    return cantidadLitros * precioPintura


PRECIO_ALFOMBRA_M2 = 104
PRECIO_PINTURA_LITRO = 83

metrosLargo = int(input("Introduzca el largo del cuarto:\t>"))
metrosAncho = int(input("Introduzca el ancho del cuarto:\t>"))
metrosAlto = int(input("Introduzca el alto del cuarto:\t>"))

superficieParedes = superficieParedes(metrosAlto, metrosAncho, metrosLargo)
superficiePiso = superficiePiso(metrosAncho, metrosLargo)

print("Alfombrar el cuarto costara:\t$", costoAlfombrar(PRECIO_ALFOMBRA_M2, superficiePiso))
print("Pintar el cuarto costara:\t$", costoPintar(PRECIO_PINTURA_LITRO, superficieParedes))