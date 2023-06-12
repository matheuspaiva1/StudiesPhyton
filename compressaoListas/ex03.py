'''4 - 
Inicialize uma lista de 20 números inteiros. Armazene
os números pares em uma lista PAR e os números
ímpares em uma lista IMPAR. Imprima as listas PAR
e IMPAR. '''
#####################################################
numeros = [int(indice) for indice in input().split()]

if len(numeros) <= 20:
  par = [indice for indice in numeros if indice % 2 == 0]

  impar = [indice for indice in numeros if indice % 2 != 0]

  print(par)

  print(impar)
else:
   print("reinicie")