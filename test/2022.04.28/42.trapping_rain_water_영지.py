height = [0,1,0,2,1,0,1,3,2,1,2,1]

# 리스트 > 정수
if not height :
    print(0)

start = 0
end = len(height)-1

water = 0
 
while 1 :
    # if end == len(height) :;'
        # break 
    if height[end-1] - height[end]  >= 0 : #하강
        end += 1
    else : #상승
        if height[end] - height[end+1] >= 0 : #다음에서 하강히는 경우
            m = min(height[end],height[start])
            for j in range(start+1,end-1) :
                water = m - height[j] 
                # pass #작은거 높이만큼 물채우기 
            start = end
        #계속상승하는 경우
        end += 1