candidates = [2,3,6,7]
target = 7

result = []
ans = []
def dfs():
    global target
    if sum(ans) == target :
        result.append(ans[:])
        return 
    elif sum(ans) > target :
        return

    for i in range(len(candidates)) :
        ans.append(candidates[i])
        dfs()
        ans.pop()
    
dfs()
result = [sorted(i) for i in result]
result = list(set([tuple(i) for i in result]))
print(result)

    