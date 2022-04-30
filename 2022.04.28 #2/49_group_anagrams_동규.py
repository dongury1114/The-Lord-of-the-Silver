#이중 배열로 출력
#원소들의 구성요소가 같은것 끼리 묶기
#각각의 원소를 정렬을 통해 같은지 비교 -> 딕셔너리를 이용하면 쉽게 가능

#sol.1
from collections import defaultdict
strs = ["eat","tea","tan","ate","nat","bat"]
ans = defaultdict(list) # 아이디어 참고 (애용하겠습니다!)


for i in strs:
    ans[''.join(sorted(i))].append(i)
    

print(list(ans.values()))

#sol.2
from collections import defaultdict
strs = ["eat","tea","tan","ate","nat","bat"]

anagrams = defaultdict(list)
for string in strs:
    anagrams[tuple(sorted(string))].append(string) 
print(anagrams)
