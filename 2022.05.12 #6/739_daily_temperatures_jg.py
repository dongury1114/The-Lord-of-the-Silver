class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in range(len(temperatures))]
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                pop = stack.pop()
                result[pop] = i - pop
            stack.append(i)
        return (result)
        # max_temp = 101
        # for i in range(len(temperatures) - 1):
        #     left = i
        #     right = i+1
        #     cnt = 1
        #     if max_temp <= temperatures[left]:
        #         result.append(0)
        #         continue
        #     else:
        #         while left >= 0 and right < len(temperatures) and temperatures[left] >= temperatures[right]:
        #             right += 1
        #             cnt += 1
        #     if right == len(temperatures):
        #         cnt = 0
        #         max_temp = temperatures[left]
        #     result.append(cnt)
        # result.append(0)
        # return (result)
