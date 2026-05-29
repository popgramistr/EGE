min_d = 200
p = range(117, 158)
q = range(130, 180)

for begin in range(200):
    for end in range(200):
        a = range(begin, end)
        if all((x in p) <= (( (not (x in a)) and (x in q) ) <= (not (x in p))) for x in range(200)):
            min_d = min(min_d, end - begin)
print(min_d)