#sol.01 (내 풀이)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse() # s[:] = s[::-1]


#sol.02
class Solution:
    def reverseString(self, s: List[str]) -> None:
        start, end = 0, len(s)-1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1


#sol.03
class Solution:
    def reverseString(self, s: List[str]) -> None:

        size = len(s)
        for i in range(size//2):
            s[i], s[-i-1] = s[-i-1], s[i]