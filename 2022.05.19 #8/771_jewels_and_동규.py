jewels = "aA"
stones = "aAAbbbb"

jewels = list(jewels)
stone = list(stones)
count = 0
for i in jewels:
    for j in stone:
        if i == j:
            count += 1
print(count)
