def listaInts(L):
    p = len([x for x in L if x % 2==0 and x != 0])
    i = len([x for x in L if x %2 == 1])
    z = L.count(0)
    
    return p, i, z
    

lista = [int(i) for i in input().split()]


a,b,c = listaInts(lista)

print(a,b,c)
