'''3 - 
receber um vetor com 20 idades e exibir a
maior e menor.'''
##############################################################
idades = [int(idade) for idade in input().split()]

L = [print(max(idades), min(idades)) if len(idades) <= 20 else print("reinicie")]

## OU ##

if len(idades) <= 20: 
  print(max(idades), min(idades))
else:
  print("reinicie")
