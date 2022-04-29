#소스: https://medium.com/leetnotes/leetcode-42-trapping-rain-water-b8e325e72167

class Solution(object):
    def trap(self, height):
        res = 0
        max_left, max_right = 0, 0
        left, right = 1, len(height)-2
        while left <= right:
            max_left = max(max_left, height[left-1])
            max_right = max(max_right, height[right+1])
            if max_left <= max_right:
                if max_left > height[left]:
                    res += max_left - height[left]
                left += 1
            else:
                if max_right > height[right]:
                    res += max_right - height[right]
                right -= 1     
        return res




height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap(height))