frase = input("digite uma frase: ")

listPalavras = frase.split()

print("há", len(listPalavras), "palavras")

soma = 0

for palavra in listPalavras:
	soma += len(palavra)
print("the averge word length is", soma/len(listPalavras))
