nums = [3, 30, 34, 5, 9]


# sol.02
class Solution:


def largestNumber(self, nums: List[int]) -> str:
    return str(int(''.join(sorted(map(str, nums), key=lambda s: s*10)[::-1])))
