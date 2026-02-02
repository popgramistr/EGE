from itertools import product

count = 0
gl = 'ЕАИ'
sogl = 'ГРСМ'
for s in product(gl, sogl, gl, sogl, gl, sogl, gl):
    line = ''.join(s)
    if len(set(line)) == len(line):
        count += 1

for s in product(sogl, gl, sogl, gl, sogl, gl, sogl):
    line = ''.join(s)
    if len(set(line)) == len(line):
        count += 1

print(count)