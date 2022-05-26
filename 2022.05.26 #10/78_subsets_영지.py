from typing import List

nums = [1,2,3]

result = [[]]
def dfs(ans,index):
    if ans :
        result.append(ans)

    for i in range(index,len(nums)) :
        dfs(ans+[nums[i]],i+1)

dfs([],0)

print(result)


