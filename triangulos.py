def triangulo(a, b, c):
    if a + b >= c and b + c >= a and a + c >= b:
        return "SIM"
    else:
        return "NAO"
x1 = int(input())
x2 = int(input())
x3 = int(input())

print(triangulo(x1, x2, x3))