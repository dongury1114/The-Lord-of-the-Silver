class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(elem):
            if len(elem) == 0:
                result.append(prev_elem[:])
            
            for e in elem:
                next_elem = elem[:]
                next_elem.remove(e)
                
                prev_elem.append(e)
                dfs(next_elem)
                prev_elem.pop()
        
        result = []
        prev_elem = []
        dfs(nums)
        return (result)
        # return list(itertools.permutations(nums))
