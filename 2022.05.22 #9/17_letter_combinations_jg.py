class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        nums = {
            '2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
        }
        def dfs(index, string):
            if len(string) == len(digits):
                result.append(string)
                return
            for i in range(index, len(digits)):
                for j in nums[str(digits[i])]:
                    dfs(i+1, string + j)
        if not len(digits):
            return []
        dfs(0, "")
        return (result)
                    
