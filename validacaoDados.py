def ePar(num):
    if num % 2 == 0:
        return True
    else:
        return False
        
def mult8(num):
    if num % 8 == 0:
        return True
    else:
        return False
while True:
    x1 = int(input())
    
    if ePar(x1):
        if mult8(x1):
            print("O número é par, mas é múltiplo de 8. Informe um número par não múltiplo de 8.")
        elif not mult8(x1):
            print("O número fornecido foi {} e ele é par e não múltiplo de 8.".format(x1))
            break
    else:
        print("O número não é par. Informe um número par não múltiplo de 8.")

        
    