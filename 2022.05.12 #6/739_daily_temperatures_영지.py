
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]


# 시간초과

# answer = []

# for i in range(len(temperatures)) :
#     day = 0
#     for j in range(i+1, len(temperatures)) :
#         if temperatures[j] > temperatures[i] :
#             day = j-i
#             break
#     answer.append(day)

# print(answer)


# 스택 사용해서 풀기

answer = [0] * len(temperatures)
stack = []  # 임시 저장소로 사용하기

for i, cur in enumerate(temperatures):
    while stack and cur > temperatures[stack[-1]]:
        last = stack.pop()
        answer[last] = i - last
    stack.append(i)  # 스택에 인덱스 넣기

print(answer)
