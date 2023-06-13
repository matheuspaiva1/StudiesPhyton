import random

smallerNumber = int(input("enter small number: "))
largerNumber = int(input("enter larger number: "))	

randomNumber = random.randint(smallerNumber, largerNumber)
count = 0

while True :
	count += 1
	userNumber = int(input("enter your guess: "))
	
	if userNumber < randomNumber :
		print("too small")
	elif userNumber > randomNumber:
		print("too larger")
	else:
		print("concluiu em ", count, "tentativas")
		
		break	
