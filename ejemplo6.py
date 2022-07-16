def cargar_datos():
    articulos = []
    precios = []
    for x in range(5):
        ar = input("Ingrese el nombre del articulo: ")
        articulos.append(ar)
        pre = int(input("Ingrese el precio de dicho articulo: "))
        precios.append(pre)
    return [articulos, precios]


def imprimir(articulos, precios):
    print("Listado completo de articulos y sus profuctos: ")
    for x in range(len(articulos)):
        print(articulos[x], precios[x])

def precio_mayor(articulos, precios):
    may = precios[0]
    pos = 0
    for x in range(len(precios)):
        if precios[x] > may:
            may = precios[x]
            pos = x
    print("Articulo con un precio mayor es: ", articulos[pos],"su precio es: ", may)



def consulta_precio(articulos, precios):
    valor = int(input("Ingrese en importe para mostrar los articulos con un precio menor: "))
    for x in range(len(articulos)):
        if precios[x] < valor:
            print(articulos[x], precios[x])


#bloque principal del programa


articulos, precios = cargar_datos()
imprimir(articulos, precios)
precio_mayor(articulos, precios)
consulta_precio(articulos, precios)