class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = collections.defaultdict(int)
        
        for num in nums:
            result[num] += 1
            
        for key, value in result.items():
            if value == 1:
                return key
                
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        
        for num in nums:
            result ^= num
            
        return result