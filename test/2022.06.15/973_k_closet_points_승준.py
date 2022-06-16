class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = list()
        real_result = list()
            
        for i in range(len(points)):
            tmp = points[i][0]**2 + points[i][1]**2
            result.append((tmp, i))
            
        result.sort()
        
        for j in range(k):
            real_result.append(points[result[j][1]])
            
        return real_result