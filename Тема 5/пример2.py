a = set()
for N in range(10, 1001):
    R = bin(N)[2:]
    if R[0] == '1':
        R = R[1:]
        R = R.lstrip('0')
    if R == '':
        R = '0'
    R = int(R, 2)
    num = N - R
    a.add(num)
print(len(a))