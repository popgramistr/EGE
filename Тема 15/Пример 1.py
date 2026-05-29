for a in range(16384):
    if all((x & 6280 > 0 or x & 3394 > 0) <= ((x & 10828 == 0) <= (x & a > 0)) for x in range(16384)):
        print(a)
        break