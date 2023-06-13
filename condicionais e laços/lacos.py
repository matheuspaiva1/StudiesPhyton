''' 
 * FOR
 for <variável> in range(<uma expressão inteira>): 
 <instrução-1> 
 . 
 .
 <instrução-n>
'''

number = int(input('digite um numero '))
exponent = int(input('digite o exponente '))
product = int(input('digite o produto '))

for eachpass in range(exponent):
	product = product * number
	print(product, end = ' ')



product = 1

for count in range(3, 7):
	product = product * (count + 1)
	print(product)




lower = int(input("digite o lower "))
upper = int(input("digite o upper "))

theSum = 0

for number in range(lower, upper + 1):
	theSum = theSum + number
	print(theSum)





list(range(1, 6, 1)) # O mesmo que usar dois argumentos

>>> list(range(1, 6, 2)) # Usa cada segundo número
[1, 3, 5]

>>> list(range(1, 6, 3)) # Usa cada terceiro número 
[1, 4]



# [contagem regressiva]
for count in range(10, 0, -1): 
	print(count, end = " ")

