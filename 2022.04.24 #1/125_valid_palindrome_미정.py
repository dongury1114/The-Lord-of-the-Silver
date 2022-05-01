class Solution:  
    def isPalindrome(self,s):    
        s = s.lower()
        s = ''.join(e for e in s if e.isalnum()) #alphanumeric 인 경우에만 합치기
        return s == s[::-1] 

