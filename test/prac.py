numbers = [2, 3, 4]
target = 6

for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        if numbers[i]+numbers[j] == target:
            ans = [i+1, j+1]
print(ans)
