def f(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    c = str(x)
    if c[0] > c[1]:
        c = c[1] + c[0]
        c = int(c)
        return f(x - 3, y) + f(c, y)
    else:
        return f(x - 3, y)

print(f(43, 13))