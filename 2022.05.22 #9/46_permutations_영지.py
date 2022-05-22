import itertools
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums,len(nums)))

nums = [1,2,3]

result = []
permute = []
def dfs():
    if len(permute) == len(nums) :
        result.append(permute[:])
        return
    
    for i in range(len(nums)) :
        if nums[i] not in permute :
            permute.append(nums[i])
            dfs()
            permute.pop()

dfs()
print(result)

