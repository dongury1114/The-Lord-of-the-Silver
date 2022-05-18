# tmmzuxtat
# abcabcbb

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lt = 0
        result = 0
        seen = dict()
        
        for rt, x in enumerate(s):
            if x in seen and lt <= seen[x]:
                lt = seen[x] + 1
            else:
                result = max(result, rt - lt + 1)
                
            seen[x] = rt
        
        return result