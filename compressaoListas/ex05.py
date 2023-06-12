'''Implemente um programa que formatar um texto.

Implemente um programa que recebe um texto e depois um código representando uma formatação que deve ser aplicado no texto.

As formatações aplicadas serão:

M - Toda maiúscula
m - toda minúscula
P - Apenas a primeira letra de cada palavra deve está em maiúscula, palavras de tamanho maior que 2, exceto se ela for a primeira, então ficará maiúscula independente do seu tamanho.
A entrada será um texto e depois um caractere representando a formatação (M ou m ou P).
#############################################################################
'''
texto = input()
formats = input()
regras = ['M', 'm', 'p']

if formats == regras[0]:
    print(texto.upper())
elif formats == regras[1]:
    print(texto.lower())
elif formats == regras[2]:
    print(texto.title())
