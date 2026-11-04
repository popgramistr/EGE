nums = list(map(int, open("Пример 1.txt").readlines()))
kr32 = 0
max_sum = -10000000
count = 0

for i in nums:
    if i % 32 == 0:
        kr32 += 1

for i in range(len(nums) - 1):
    a = nums[i]
    b = nums[i + 1]
    if (a < 0 or b < 0) and (a + b < kr32):
        count += 1
        max_sum = max(max_sum, a + b)

print(count, max_sum)