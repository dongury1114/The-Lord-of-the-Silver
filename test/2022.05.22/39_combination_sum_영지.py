candidates = [2,3,6,7]
target = 7

result = []

def dfs(index, ans):
    global target
    if ans and sum(ans) == target :
        result.append(ans[:])
        return 
    elif ans and sum(ans) > target :
        return

    for i in range(index, len(candidates)) :
        dfs(i, ans + [candidates[i]])
        # ans.pop()
    
dfs(0,[])
# result = [sorted(i) for i in result]
# result = list(set([tuple(i) for i in result]))
print(result)


# def dfs():
#     pass