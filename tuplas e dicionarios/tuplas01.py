def listaInts(lista,key):
    repet = lista.count(key)
    for i in lista:
        if i % key == 0:
            repet2 = i.count(key)
    return repet, repet2

lista = [int(i) for i in input().split()]
key = int(input())

cont,mult = listaInts(lista, key)