def solution(n, arr1, arr2):
    result = list()
    
    for i in range(n):
        result.append(bin(arr1[i] | arr2[i])[2:].zfill(n).replace('1', '#').replace('0', ' '))
        
    return result
    
    
# 테스트1, 테스트3 런타임 에러 혹은 시간 초과 발생    
def solution(n, arr1, arr2):    
    def to_binary(x, temp):
        if x == 1:
            temp.append(1)
            return temp
        
        to_binary(x // 2, temp)
        temp.append(x % 2)
        
        return temp
    
    def arr_to_binary(arr):
        result = list()
        
        for num in arr:
            temp = to_binary(num, list())
            
            if num != 0:
                temp = to_binary(num, list())

                if len(temp) < n:
                    for _ in range(n - len(temp)):
                        temp.insert(0, 0)
            
            else:
                temp = list()
                for _ in range(n):
                    temp.append(0)
                    
            result.append(temp)
            
        return result
    
    arr1 = arr_to_binary(arr1)
    arr2 = arr_to_binary(arr2)
    
    result = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if arr1[i][j] or arr2[i][j]:
                result[i][j] = '#';
                
            else:
                result[i][j] = ' ';
    
    real_result = list()
    
    for k in result:
        real_result.append("".join(k))
        
    return real_result
    

    