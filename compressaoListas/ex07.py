'''
Implemente um programa que irá receber uma lista de inteiros. Obrigatoriamente armazene esses números numa lista.

Depois será informado dois índices válidos da lista, com o segundo sendo maior ou igual ao primeiro. 

Usando fatiamento (não pode usar for e nem while), gere uma nova lista com todos os elementos da lista de entrada, começando do primeiro índice até o segundo índice.

Vamos com um exemplo. Suponha a seguinte lista de entrada: [472, 539, 220, 113, 368, 450] e dos dois índices 2 e 4. A nova lista será [220, 113, 368].
############################################################################################'''
numeros = [int(num) for num in input().split()]

indice1 = int(input())
indice2 = int(input())


if indice2 >= indice1:
    print(numeros[indice1+1:indice2-2])
