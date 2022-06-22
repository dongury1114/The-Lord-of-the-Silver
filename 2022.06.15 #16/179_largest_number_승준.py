class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def _change(x, y):
            tmp1 = str(x) + str(y)
            tmp2 = str(y) + str(x)
            
            if tmp2 > tmp1:
                return False
            else:
                return True
            
        for i in range(1, len(nums)):
            for j in range(i, 0, -1):
                if _change(nums[j], nums[j - 1]):
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
                    
        result = str(int(''.join(map(str, nums))))

        return result