class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        visited = [0] * 3
        
        for i in range(len(nums)):
            if nums[i] == 0:
                visited[0] += 1
            elif nums[i] == 1:
                visited[1] += 1
            else:
                visited[2] += 1
                
        result = list()
        
        for j in range(len(visited)):
            while (visited[j] != 0):
                visited[j] -= 1
                result.append(j)
                
        print(result)
        
        return result
        
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        red = 0
        white = 0
        blue = len(nums)
        
        while white < blue:
            if nums[white] < 1:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            
            elif nums[white] > 1:
                blue -= 1
                nums[white], nums[blue] = nums[blue], nums[white]
            else:
                white += 1
            