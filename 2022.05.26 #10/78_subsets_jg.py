class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # def dfs(l, r):
            # if not l:
            #     result.append(l[:])
            #     return
            # result.append(l[:])
            # pop = l.pop()
            # result.append([pop])
            # r.append(pop)
            # result.append(r[:])
            # dfs(l, r)
        def dfs(index, string):
            result.append(string)
            for i in range(index, len(nums)):
                dfs(i+1, string+[nums[i]])
        result = []
        dfs(0, [])
        return (result)
