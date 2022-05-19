
from collections import Counter


nums = [1, 1, 1, 2, 2, 3]
k = 2

# c = dict()
# for i in sorted(nums) :
#     c[i] = nums.count(i)

# c = sorted(c.items(), key=lambda x:x[1],reverse=True)[:k]

# result = [x[0] for x in c]
# print(result)

c = Counter(nums)
c = sorted(c.items(), key=lambda x: x[1], reverse=True)[:k]

result = [x[0] for x in c]
print(result)
