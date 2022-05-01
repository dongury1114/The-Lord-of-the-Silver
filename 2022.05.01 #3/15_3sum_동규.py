#메모리 초과.. 
from itertools import combinations

nums = [-1,0,1,2,-1,-4]

tmp = list(combinations(nums, 3))

ans = []

result = []
for i in range(len(tmp)):
    if sum(tmp[i]) == 0:
        ans.append(sorted(tmp[i]))

ans = list(set([tuple(ans) for ans in ans]))

# ans = list(set(ans))
print(ans)

# print(ans)
# for i in range(len(ans)):

#처음에 브루트포스로 생각했으나, 시간초과가 날것 같음

#투포인터

#슬라이딩 윈도우와 투포인터 비교 설정 드가자

