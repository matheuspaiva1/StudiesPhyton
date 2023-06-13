import math


area = float(input("digite a area "))

if area > 3 :
	calculo = math.sqrt(area/math.pi)
	print(calculo)
else :
	print("ERROR")


first = int(input("diga o primeiro numero "))
second = int(input("diga o segundo numero "))

if first > second :
	maximum = first
	minimum = second
else :
	minimum = first
	maximum = second

print("maximo: ", maximum)
print("minimo: ", minimum)

# OU

first = int(input("Enter the first number: ")) 
second = int(input("Enter the second number: ")) 

print("Maximum:", max(first, second)) 
print("Minimum:", min(first, second)


number = int(input("Enter the numeric grade: ")) 

if number > 89: 
	letter = 'A'
	 
elif number > 79: 
	letter = 'B'
	 
elif number > 69: 
	letter = 'C'
	
else: 
	letter = 'F'
	
print("The letter grade is", letter) 

# EXPRESSÕES BOOLEANAS (OR, AND E NOT)
