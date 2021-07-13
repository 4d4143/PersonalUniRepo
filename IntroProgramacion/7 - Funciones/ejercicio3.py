#diseniar una funcion que calcule el triple de un numero y otra que calcule el siguiente
#utilizar las funciones para que ingresado un numero, se muestre el consecutivo del triple
# y el triple del consecutivo de ese numero

def tripleNumero(numero):
    return numero * 3

def consecutivoNumero(numero):
    return numero + 1

print("Ejemplo con 100")
print("El triple del consecutivo de 100:\t", tripleNumero(consecutivoNumero(100)))
print("El consecutivo del triple de 100:\t", consecutivoNumero(tripleNumero(100)))