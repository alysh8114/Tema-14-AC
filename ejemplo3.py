def producto(lista):
    prod = 1
    for x in range(len(lista)):
        prod = prod * lista[x]
    return prod


#bloque principal del programa

lista = [1, 2, 3, 4, 5]
print("Lista: ", lista)
print("Multiplicacion de todos los elementos: ", producto(lista))
