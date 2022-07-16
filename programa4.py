"""En una empresa se almacenaron los sueldos de 10 personas.
Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
Carga de los sueldos en una lista.
Impresión de todos los sueldos.
Cuántos tienen un sueldo superior a $4000.
Retornar el promedio de los sueldos.
Mostrar todos los sueldos que están por debajo del promedio."""

def cargar_sueldos():
    sueldos = []
    for x in range(10):
        sueldo = int(input("Ingrese el sueldo: $"))
        sueldos.append(sueldo)
    return sueldos

def imprimir_sueldos(sueldos):
    print("Lista de sueldos")
    for x in range(len(sueldos)):
        print(sueldos[x])

def sueldos_mayor4000(sueldos):
    cantidad = 0
    for x in range(len(sueldos)):
        if sueldos[x] > 4000:
            cantidad = cantidad + 1
    print("Cantidad de empleados con un sueldo mayor a $4000: ", cantidad)


def promedio(sueldos):
    suma = 0
    for x in range(len(sueldos)):
        suma = suma + sueldos[x]
    promedio = suma//10
    return promedio


def sueldos_bajos(sueldos):
    pro = promedio(sueldos)
    print("Sueldos inferiores al promedio: ",pro)
    for x in range(len(sueldos)):
        if sueldos[x] < pro:
            print(sueldos[x])


#bloque principal
sueldos = cargar_sueldos()
imprimir_sueldos(sueldos)
sueldos_mayor4000(sueldos)
sueldos_bajos(sueldos)
