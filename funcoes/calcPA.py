def p_a(a1, r, n):
    an = a1 + (n-1) * r
    return an
x1 = int(input())
x2 = int(input())
x3 = int(input())

print(p_a(x1, x2, x3))
    