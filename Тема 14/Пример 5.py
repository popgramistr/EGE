a = 19 ** 270 + 19 ** 240 + 19 ** 190 + 19 ** 180
x = 0
while True:
    count = 0
    x += 1
    c = a - x
    while c > 0:
        if c % 19 == 18:
            count += 1
        c //= 19
    if count == 177:
        print(x)
        break
    print('Цикл: ', x)