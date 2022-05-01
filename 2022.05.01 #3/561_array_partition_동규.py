nums = [1,4,3,2]

nums.sort()

# 2개씩 묶어서 min 치기
# 슬라이싱(?)
# 짝수 번째가 항상 최솟값
s = []

for i in range(len(nums)):
    if i % 2 == 0:
        s.append(nums[i])
print(sum(s))