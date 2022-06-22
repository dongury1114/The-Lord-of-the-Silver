from itertools import permutations


nums = [3, 30, 34, 5, 9, 90, 97]
nums = list(map(str, nums))

<<<<<<< HEAD
s_num = sorted(nums, key= lambda x:x*2)[::-1]
=======
s_num = sorted(nums, key=lambda x: int(x)*10)[::-1]
>>>>>>> 43f6e45c6c511686879b3582fe19e3d939a2f584

print(s_num)
