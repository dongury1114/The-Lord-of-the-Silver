class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = {}
        max_length = start = 0
        for index, num in enumerate(s):
            if num in ans and start <= ans[num]:
                start = ans[num] + 1
            else: 
                max_length = max(max_length, index-start+1)
            ans[num] = index
        return max_length