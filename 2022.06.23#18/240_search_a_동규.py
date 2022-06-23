class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    count += 1
                    break
        if count >= 1:
            return True
        else:
            return False


def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    # i, j = len(matrix) - 1, 0
    # while(i >= 0 and i < len(matrix) and j >=0 and j < len(matrix[0])):
        if(matrix[i][j] == target): return True
        if(matrix[i][j] > target):  i -= 1
        if(matrix[i][j] < target):  j += 1
    return False
