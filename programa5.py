"""Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne.
Una segunda función debe recibir una lista y retornar el mayor y el menor valor de la lista.
Desde el bloque principal del programa llamar a ambas funciones e imprimir el mayor y el menor de la lista."""

def mayor_menor(lista):
    may = lista[0]
    men = lista[0]
    for x in range(1,len(lista)):
        if lista[x] > may:
            may = lista[x]
        else:
            if lista[x] < men:
                men = lista[x]
    print("El mayor valor de la lista es", may)
    print("El menor valor de la lista es",men)

#bloque principal del programa
lista = []
for x in range(5):
    valor = int(input("Ingrese el valor: "))
    lista.append(valor)
mayor_menor(lista)