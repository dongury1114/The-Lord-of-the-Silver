# 책 풀이 참고 - defaultdict 활용
from typing import List     # 해당 라이브러리 사용 시 vscode에서 노란 줄(List에 뜨는) 사라짐.
from collections import defaultdict

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         res = defaultdict(list)
        
#         for str in strs:
#             res[''.join(sorted(str))].append(str)
            
#         return res.values()
        


# defaultdict 활용 X
# defaultdict를 사용한 것과 비교 시, 런타임 및 메모리에서 거의 차이 없음.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_dict = dict()
        res_list = list()

        for str in strs:
            str_joined = ''.join(sorted(str))
            
            if str_joined not in res_dict.keys():
                res_dict[str_joined] = list()
                
            res_dict[str_joined].append(str)
            
        for value in res_dict.values():
            res_list.append(value)
            
        return res_list