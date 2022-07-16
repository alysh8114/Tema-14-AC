"""Confeccionar un programa que permita:
Cargar una lista de 10 elementos enteros.
Generar dos listas a partir de la primera. En una guardar los valores positivos y en otra los negativos.
Imprimir las dos listas generadas."""

def cargar():
    lista = []
    for x in range(10):
        valor = int(input("Ingrese un valor: "))
        lista.append(valor)
    return lista


def generar_lista():
    lisnegativo = []
    lispositivo = []
    for x in range(len(lista)):
        if lista[x] <0:
            lisnegativo.append(lista[x])
        else:
            if lista[x] > 0:
                lispositivo.append(lista[x])
    return [lisnegativo, lispositivo]


def imprimir (lista):
    for x in range(len(lista)):
        print(lista[x])

#bloque principal
lista = cargar()
lisnegativo, lispositivo = generar_lista()
print("Lista con los valores negativos: ")
imprimir (lisnegativo)
print("Lista con los valores positivos: ")
imprimir (lispositivo)
