from itertools import product

# ������ �������� ��� ������ product
print('x y z w')
for x, y, z, w in product([1, 0], repeat=4):
    if not((not(z) == y) <= ((w and not(x)) == (y and x))):
        print(x, y, z, w)