from collections import defaultdict

graph = defaultdict(list)
tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"],
           ["ATL", "JFK"], ["ATL", "SFO"]]  # 그래프 순서대로 구성
for a, b in sorted(tickets):
    graph[a].append(b)


route = []


def dfs(a):
    # 첫 번째 값을 읽어 어휘순 방문
    while graph[a]:
        dfs(graph[a].pop(0))
    route.append(a)


dfs('JFK')
# 다시 뒤집어 어휘순 결과로
print(route[::-1])

# sol.2
# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#         graph = collections.defaultdict(list)
#         # 그래프 뒤집어서 구성
#         for a, b in sorted(tickets, reverse=True):
#             graph[a].append(b)

#         route = []

#         def dfs(a):
#             # 마지막 값을 읽어 어휘순 방문
#             while graph[a]:
#                 dfs(graph[a].pop())
#             route.append(a)

#         dfs('JFK')
#         # 다시 뒤집어 어휘순 결과로
#         return route[::-1]
# sol.01
# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#         #lincked list(?)
#         #모든 시작은 JFK
#         # 사전순...
#         #DFS 는 맞는거 알겠다, but how to solve it
#         #root는 항상 JFK
#         targets = collections.defaultdict(list)
#         for a, b in sorted(tickets)[::-1]:
#             targets[a] += b,
#         route, stack = [], ['JFK']
#         while stack:
#             while targets[stack[-1]]:
#                 stack += targets[stack[-1]].pop(),
#             route += stack.pop(),
#         return route[::-1]
