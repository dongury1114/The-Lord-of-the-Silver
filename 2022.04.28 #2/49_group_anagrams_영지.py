
strs = ["a"]

result = dict()

for i in range(len(strs)) :
    a = sorted(strs[i])
    if ''.join(a) in result.keys() :
        result[''.join(a)].append(i)
    else : result[''.join(a)] = [i]

# print(len(result.values()))

grouping = [[] for _ in range(len(result))]

for i in range(len(result)) :
    for j in list(result.values())[i] :
        # print(j)
        grouping[i].append(strs[j]) 

# print(grouping)