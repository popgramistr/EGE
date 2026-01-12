R = 1

N = 100
while R % 4 != 0:
    R = bin(N)[2:]
    for i in range(3):
        one = R.count('1')
        zero = R.count('0')
        if one == zero:
            R = R + R[-1]
        elif one > zero:
            R = R + '0'
        else:
            R = R + '1'
    R = int(R, 2)
    N += 1
print(N - 1)