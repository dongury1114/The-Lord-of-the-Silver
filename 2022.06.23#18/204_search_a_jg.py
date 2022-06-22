class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for i in matrix:
        #     for j in i:
        #         if j == target:
        #             return True
        # return False
         
        def find(n, target):
            start = 0
            end = len(n) - 1
            while start <= end:
                mid = (start + end) // 2

                if n[mid] == target:
                    return 1
                elif n[mid] > target:
                    end = mid - 1
                else:
                    start = mid +1
            return 0
        
        for i in matrix:
            if i[-1] < target:
                continue
            if(find(i, target)):
                return True
        return False
    
        