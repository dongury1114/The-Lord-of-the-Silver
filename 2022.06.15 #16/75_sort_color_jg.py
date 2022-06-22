class Solution:
    def q(self, nums):
        if len(nums) <= 1:
            return nums
        pivot = nums[len(nums)//2]
        left, same, right = [], [], []
        for n in nums:
            if n < pivot:
                left.append(n)
            elif n > pivot:
                right.append(n)
            else:
                same.append(n)
        return self.q(left) + same + self.q(right)
    
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #삽입
        # i = 1
        # while i < len(nums):
        #     j = i
        #     while j > 0:
        #         if nums[j-1] > nums[j]:
        #             nums[j-1], nums[j] = nums[j], nums[j-1]
        #         j -= 1
        #     i += 1
        #퀵
        result = self.q(nums)
        llist = [num for num in result]
        print(llist)
        return llist# class Solution:
def sortColors(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    #삽입
    # i = 1
    # while i < len(nums):
    #     j = i
    #     while j > 0:
    #         if nums[j-1] > nums[j]:
    #             nums[j-1], nums[j] = nums[j], nums[j-1]
    #         j -= 1
    #     i += 1
    #퀵
    if len(nums) <= 1:
        return nums
    pivot = nums[len(nums)//2]
    left, same, right = [], [], []
    for n in nums:
        if n < pivot:
            left.append(n)
        elif n > pivot:
            right.append(n)
        else:
            same.append(n)
    return sortColors(left) + same + sortColors(right)

print(sortColors([2,0,2,1,1,0]))
