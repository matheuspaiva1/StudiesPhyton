def maior(a, b, c):
    if b < a > c:
        return a
    elif b > c:
        return b
    else:
        return c
   
        
x1 = int(input())
x2 = int(input())
x3 = int(input())

print(maior(x1, x2, x3))