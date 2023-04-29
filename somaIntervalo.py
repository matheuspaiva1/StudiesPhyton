def somaIntervalo(a, b):
    soma = 0
    i = a
    while i <= b:
        soma += i
        i += 1      
    return soma
x1 = int(input())
x2 = int(input())
print(somaIntervalo(x1, x2))
    