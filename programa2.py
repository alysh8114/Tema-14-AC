"""Desarrollar una función que reciba una lista de string y nos retorne el que tiene más caracteres.
Si hay más de uno con dicha cantidad de caracteres debe retornar el que tiene un valor de componente más baja.
En el bloque principal iniciamos por asignación la lista de string."""

def mas_caracteres(lista):
    mas = 0
    for x in range(1,len(lista)):
        if len(lista[x]) > len(lista[mas]):
            mas = x
        else:
            if len(lista[x]) == len(lista[mas]):
                if lista[x] > lista[mas]:
                    mas = mas
                else:
                    pos = x
    return lista[mas]

#bloque principal
palabaras =["Desarrollo", "Soporte", "Algoritmo", "Diseño", "Laboratorio"]
print(palabaras)
print("Palabras con mas caracteres:", mas_caracteres(palabaras))
