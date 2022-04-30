class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = list(filter(str.isalnum,s))
        if (''.join(c)).upper() == (''.join(c[::-1])).upper() :
            return True
        else :
            return False
        
# import sys

# s = input()
# Solution().isPalindrome(s)
