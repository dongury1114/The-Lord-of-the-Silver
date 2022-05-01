# 소스: https://velog.io/@jzizsuuz/LeetCode238.-Product-of-Array-Except-Self-python

class Solution(object):
    def productExceptSelf(self, nums):

        output = []
        
        temp = 1
        # 자기 자신을 제외하고 왼쪽에 있는 값 곱셈
        for i in range(len(nums)):
            output.append(temp)
            temp *= nums[i]
        
        temp = 1
        # 자기 자신을 제외하고 오른쪽에 있는 값 곱셈
        for i in range(len(nums)-1,-1,-1): # nums를 거꾸로 탐색
            output[i] *= temp # 메모리 공간 절약을 위해 output에 바로 저장
            temp *= nums[i] 
        
        return output         