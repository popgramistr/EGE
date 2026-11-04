# Решение

nums = list(map(int, open("Задание 1702.txt").readlines()))
count = 0
m = 0

for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        a, b = nums[i], nums[j]
        if a < b:
            a, b = b, a
        if ( (a - b) % 60 == 0 ) and ( (a % 15 == 0) or (b % 15 == 0) ):
            count += 1
            m = max(m, a - b)

print(count, m)

answer1 = 63517
answer2 = 9960

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(17, 1702, f'{answer1} {answer2}', '1f1b321d4ee0f8a0a2de5ccf29035748'))