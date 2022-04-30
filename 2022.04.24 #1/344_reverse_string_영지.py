class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        a = len(s)
        for i in range(a//2) :
            s[i],s[a-i-1] = s[a-i-1],s[i]
        