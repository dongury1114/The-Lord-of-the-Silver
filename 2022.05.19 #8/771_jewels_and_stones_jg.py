class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # lop = collections.Counter(stones)
        # lop = collections.defaultdict(int)
        # result = 0
        # for s in stones:
        #     lop[s] = lop[s] + 1
        # for j in jewels:
        #     result += lop[j]
        # return (result)
        return sum(s in jewels for s in stones)
