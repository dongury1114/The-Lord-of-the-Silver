class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def _binary_search(nums, target):
            lt = 0
            rt = len(nums) - 1
            result = False
            
            while lt <= rt:
                mid = (lt + rt) // 2
                
                if nums[mid] > target:
                    rt = mid - 1
                
                elif nums[mid] < target:
                    lt = mid + 1
                    
                else:
                    result = True
                    break
                    
            return result
        
        answer = False
        
        for i in range(len(matrix)):
            if matrix[i][0] <= target:
                answer = _binary_search(matrix[i], target)
                
                if answer == False:
                    continue
                else:
                    return True
                    
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_length = len(matrix)
        col_length = len(matrix[0])
        x = 0
        y = len(matrix[0]) - 1
        result = False
        
        while 0 <= x < row_length and 0 <= y < col_length:
            if matrix[x][y] > target:
                y -= 1
            
            elif matrix[x][y] < target:
                x += 1
                
            else:
                result = True
                break
                
        return result