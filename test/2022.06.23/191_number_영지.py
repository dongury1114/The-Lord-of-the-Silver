class Solution:
    def hammingWeight(self, n: int) -> int:
        s = list(str(bin(n)))
        return s.count("1")