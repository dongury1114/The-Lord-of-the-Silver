import re
from collections import defaultdict

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

arr = re.sub('[^0-9a-zA-Z]', ' ',paragraph)
arr = list(arr.lower().split())
graph = defaultdict(int)
banned = list(map(lambda x: x.lower(), banned))

for i in arr:
    if not i in banned:
        graph[i] += 1

max = 0
result = ''

for k, v in graph.items():
    if v > max:
        max = v
        result = k
print(result)
