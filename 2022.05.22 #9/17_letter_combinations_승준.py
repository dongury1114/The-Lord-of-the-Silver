from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = list()
        digits_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
        def _DFS(start, tmp):
            if len(tmp) == len(digits):
                result.append(tmp)
                
            else:
                for i in range(start, len(digits)):
                    for j in range(len(digits_dict[digits[i]])):
                        _DFS(i + 1, tmp + digits_dict[digits[i]][j])
                
        if digits == '':
            return []
        
        _DFS(0, str())
        
        return result