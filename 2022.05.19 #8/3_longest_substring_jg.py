class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = max_l = 0
        dic = collections.defaultdict(int)
        for index, value in enumerate(s):
            if value in dic and start <= dic[value]:
                start = dic[value] + 1
            else:
                max_l = max(max_l, index - start + 1)
            dic[value] = index
        return max_l
            
