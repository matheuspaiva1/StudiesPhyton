'''Implemente um programa que recebe dois conjuntos de inteiros e imprima a interseção entre os conjuntos.

Considere que uma lista seja um conjunto.

A ordem dos elementos do conjunto interseção no vetor deve ser a mesma relativamente ao primeiro conjunto. Não considere números repetidos. É garantido que no primeiro vetor não teremos números repetidos.

Vejamos o exemplos: {2, 5, 4, 3} ∩ {2, 4} = {2, 4}, {7, 5, 2} ∩ {7, 9, 4, 7, 2, 7} = {7, 2}.

ATENÇÃO!!!!: Você obrigatoriamente devem armazenar o conjunto (lista) interseção e só depois imprimi-lo.
############################################################################################
'''
conj1 = [int(num1) for num1 in input().split()]
conj2 = [int(num2) for num2 in input().split()]

conjInt1 = [num1 for num1 in conj1 if num1 in conj2]

print(conjInt1)
