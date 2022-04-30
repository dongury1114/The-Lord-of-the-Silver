import sys
sys.stdin = open("input.txt")

class Solution():
    def reverseString(self, s):
        s[:]= s[::-1]
        return s[:]
