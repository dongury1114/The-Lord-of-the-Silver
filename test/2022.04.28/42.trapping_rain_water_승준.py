# 스택을 사용한다.
# 0이 아닌 것을 만난다면 스택에 넣는다.

datum = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
stack = list()
lt = 0
rt = 0

for idx, x in enumerate(datum):
    if x != 0:
        lt = idx
        break
        
for idx, x in enumerate(reversed(datum)):
    if x != 0:
        rt = len(datum) - idx - 1
        break
    
max_value = max(datum[lt:rt + 1])        
res = 0
for i in range(1, max_value + 1):
    for j in datum[lt:rt + 1]:
        if j < i:
            res += i - j
          
    for k in range(lt, rt + 1):
        datum[k] -= 1
        
    
print(res)

    
    
    