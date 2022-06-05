class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n <= 1:
            return [0]

        grap = defaultdict(list)

        for i in edges:
            grap[i[0]].append(i[1])
            grap[i[1]].append(i[0])

        leaves = []
        for i in range(n+1):
            if len(grap[i]) == 1:
                leaves.append(i)

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for i in leaves:
                a = grap[i].pop()
                grap[a].remove(i)

                if len(grap[a]) == 1:
                    new_leaves.append(a)

            leaves = new_leaves

        return leaves
