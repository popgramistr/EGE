a = [0] * 10**8
m = 0
for N in range(10**6):
    R = bin(N)[2:]
    N2 = N % 4
    N2 = bin(N2)[2:]
    R = R + N2
    R = int(R, 2)
    a[R] = 1
for i in range(10**8 - 65):
    m = max(m, a[i:i+65].count(1))
print(m)