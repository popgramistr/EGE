# Решение

nums = list(map(int, open("Задание 1701.txt").readlines()))
c = -1000000
count = 0
min_sum = 1000000000000

for i in nums:
    if -10000 < i < -999 and abs(i) % 9 == 0:
        c = max(c, i)
for i in range(len(nums) - 1):
    a, b = nums[i], nums[i + 1]
    if (a < 0 != b < 0) and (a + b > c):
        count += 1
        min_sum = min(min_sum, a ** 2 + b ** 2)

print(count, min_sum)

answer1 = 1
answer2 = 372436

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(17, 1701, f'{answer1} {answer2}', 'b73de31c02e01cfc4508d15f2cf61e69'))