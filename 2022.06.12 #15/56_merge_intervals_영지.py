intervals = [[1,3],[2,6],[8,10],[15,18]]

intervals.sort()
result = []
for i in intervals :
    if  result and result[-1][1] >= i[0] :
        result[-1][1] = max(i[1], result[-1][1])
    else :
        result += i,
 
print(result)