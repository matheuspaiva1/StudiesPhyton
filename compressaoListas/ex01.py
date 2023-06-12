'''
2 - 
receber uma lista com 4 notas, em seguida
o programa deve exibir as notas e a
média.
############################################################

'''

notas = [float(nota) for nota in input().split()]

L = [len(notas) if len(notas) <= 4 else "reinicie" for nota in notas ]
print(notas, sum(notas)/len(notas))
