class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alphabet_s = [0] * 26
        alphabet_t = [0] * 26
        
        for i in s:
            tmp = ord(i)
            tmp -= 97
            alphabet_s[tmp] += 1
        
        for j in t:
            tmp = ord(j)
            tmp -= 97
            alphabet_t[tmp] += 1
        
        result = alphabet_s == alphabet_t
        
        return result