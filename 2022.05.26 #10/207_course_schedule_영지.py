from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

            graph = defaultdict(list)
            for x,y in prerequisites :
                graph[x].append(y)

            def dfs(i) :
                if i in visit : #방문 체크 - 순환구조 확인
                    return False
                if i in ok : #중복체크 - 이미 순환이 없다 루트에 있는 노드는 중복 검사할필요없음
                    return True
                visit.add(i)
                for j in graph[i] : 
                    if not dfs(j) :
                        return False
                visit.remove(i)
                ok.add(i) 
                return True
            

            visit = set()
            ok = set()
            for i in list(graph) :
                if not dfs(i) :
                    return False

            return True