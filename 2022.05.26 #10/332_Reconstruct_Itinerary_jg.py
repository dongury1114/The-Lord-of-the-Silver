class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # def dfs(start):
        #     while dic[start]:
        #         dfs(dic[start].pop(0))
        #     result.append(start)
        dic = collections.defaultdict(list)
        for a, b in sorted(tickets):
            dic[a].append(b)
        result = []
        # dfs('JFK')
        stack = ['JFK']
        while stack:
            while dic[stack[-1]]:
                stack.append(dic[stack[-1]].pop(0))
            result.append(stack.pop())
        return (result[::-1])
        # def dfs(path, l):
        #     if not l:
        #         result.append(path)
        #         return
        #     for i, v in enumerate(l):
        #         if v[0] == path[-1]:
        #             path.append(v[1])
        #             del l[i]
        #             dfs(path, l)
        #     return
        # result = []
        # tickets.sort(key=lambda x:x[1])
        # # print(tickets)
        # for i, v in enumerate(tickets):
        #     if v[0] == 'JFK':
        #         del tickets[i]
        #         dfs([v[0], v[1]], tickets)
        #         break
        # if result:
        #     return result[0]
        # return []

