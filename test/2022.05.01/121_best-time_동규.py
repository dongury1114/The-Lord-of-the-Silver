# 왼쪽에서 min이 오고 오른쪽에서 max가 오면서 비교 하면 결국 투 포인터인가?
#불가능할때 0 출력

#min 의 인덱스 찾고 
#그 뒤에 있는 max찾기

#거꾸로 해서. 큰 값을 계속 갱신
prices = [7,1,5,3,6,4]

big = prices[-1]
ans = [0]
for i in range(len(prices)-1,-1,-1):
    if prices[i] < big:
        ans.append(big-prices[i])
    else:
        big = prices[i]
print((max(ans)))


