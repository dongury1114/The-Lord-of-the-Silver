#거꾸로 해서. 큰 값을 계속 갱신
class Solution(object):
    def maxProfit(self, prices):
        big = prices[-1]
        ans = [0]
        for i in range(len(prices)-1,-1,-1):
            if prices[i] < big:
                ans.append(big-prices[i])
            else:
                big = prices[i]
        return (max(ans))
