class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        data = dict()
        cnt = 0
        
        for x in stones:
            if x in jewels:
                cnt += 1
                
        return cnt