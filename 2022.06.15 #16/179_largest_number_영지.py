from itertools import permutations


nums = [3, 30, 34, 5, 9, 90, 97]
nums = list(map(str, nums))

s_num = sorted(nums, key=lambda x: int(x)*10)[::-1]

print(s_num)
