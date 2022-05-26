from itertools import combinations, product
candidates = [1, 2, 3]
target = 6

tmp = []
ans = []
for i in range(target):
    tmp.extend(list(map(list, (product(candidates, repeat=i)))))

# for i in tmp:
#     ans.append(sum(i))
print(tmp)
