# -*- coding: utf-8 -*-


def particion(lista, inicio, final):
    pivote = lista[inicio]
    izquierda = inicio+1
    derecha = final
    terminado = False

    while not terminado:
        while izquierda <= derecha and lista[izquierda] <= pivote:
            izquierda = izquierda + 1
        while lista[derecha] >= pivote and derecha >= izquierda:
            derecha = derecha - 1
        if derecha < izquierda:
            terminado = True
        else:
            temp = lista[izquierda]
            lista[izquierda] = lista[derecha]
            lista[derecha] = temp

    temp = lista[inicio]
    lista[inicio] = lista[derecha]
    lista[derecha] = temp

    return derecha


def busqueda_rapida(lista, inicio, final):
    if inicio < final:
        pivote = particion(lista, inicio, final)
        busqueda_rapida(lista, inicio, pivote-1)
        busqueda_rapida(lista, pivote+1, final)
    return lista
