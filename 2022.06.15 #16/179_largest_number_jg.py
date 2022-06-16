class Solution:
    @staticmethod
    def swap(a, b):
        return str(a) + str(b) > str(b) + str(a)
    
    def largestNumber(self, nums: List[int]) -> str:
        j = 1
        while(j < len(nums)):
            i = j
            while(i > 0):
                if not self.swap(nums[i-1], nums[i]):
                    nums[i-1], nums[i] = nums[i], nums[i-1]
                i -= 1
            j+=1
        return str(int(''.join(map(str,nums))))

