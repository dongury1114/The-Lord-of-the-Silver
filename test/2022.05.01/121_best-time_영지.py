
prices = [1,5,3,6,4]
# prices = [7,6,4,3,1]

# 백준 - 역순으로 검사하면서 작으면 다뺴고 크면 기준값 갱신 > 차이 중에 max구하기
# return int

result = [0]

i = len(prices)-1
while i > 0 :
    std=prices[i]
    for j in range(i,-1,-1) :
        if prices[j] > std :
            i = j
            break
        else:
            result.append(std-prices[j])
        if j == 0 :
            i = 0

print(max(result))