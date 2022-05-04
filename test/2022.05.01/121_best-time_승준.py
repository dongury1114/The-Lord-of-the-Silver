from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_value = prices[-1]
        res = [0]
        
        for i in range(n - 2, -1, -1):
            if prices[i] < max_value:
                res.append(max_value - prices[i])
            else:
                max_value = prices[i]
                
        return max(res)