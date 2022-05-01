nums = [1,4,3,2]

nums.sort()

sum = 0
i = len(nums)-1
while i > 0 :
    sum += min(nums[i],nums[i-1]) #어차피 정렬해서 앞에가 작은 수니까 굳이 min 할필요없음!!!!
    #sum += num[i-1]
    i -= 2

print(sum)