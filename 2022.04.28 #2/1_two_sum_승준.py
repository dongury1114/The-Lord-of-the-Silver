# 단순히 for문 2개 돌림.
# 시간 줄이는 방법을 알기 위해 책 참고

# <처음 나의 풀이>
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = list()
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    res.append(i)
                    res.append(j)
                    
        return res