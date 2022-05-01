from collections import deque

height = [0,1,0,2,1,0,1,3,2,1,2,1]

#최대 높이 만큼 돌면서
#양끝이 양수면 카운트 시작 -> 투 포인터를 활용하면 될꺼같은데 무리
#카운트: 0 보다 작은수 세기
#예제의 경우 마지막줄에 양수가 하나이기 때문에 그룹핑을 할 수 가 없다 ∴ 0

a = len(height)

height = deque(height)
count = 0 

for _ in range(1, max(height)+1): # 첫줄에서는 문제 없이 동작 
    for j in range(len(height)):
        if height[j] <= 0:
            height.popleft()
            j += 1
            break

        if height[a - 2] <= 0:
            height.pop()
            a -= 1
            break
    count += height.count(0) # 이 부분도 수정해야함 0과 음수들로
    
    for i in range(len(height)):
        height[i] -= 1
    
    print(height)


# # for hieght in range(max(height)):
# for j in range(len(height)):
#     if height[j] <= 0:
#         height.popleft()
#         j += 1
#         break

#     if height[a - 2] <= 0:
#         height.pop()
#         a -= 1
#         break

# count =height.count(0)
# print(height)
# print(count)