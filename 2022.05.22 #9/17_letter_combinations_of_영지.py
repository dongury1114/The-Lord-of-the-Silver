import itertools


digits = "23"

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num = [['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]

        if not digits : return []
        num2 = []
        for i in digits :
            i = int(i)
            num2.append(num[i-2])

        result = list(itertools.product(*num2))
        result = [''.join(i) for i in result]
        return result