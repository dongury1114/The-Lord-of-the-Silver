def solution(dartResult):
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    bonuses = {'S': 1, 'D': 2, 'T': 3}
    options = {'*': 2, '#': -1}
    current_num = -1
    result = list()
    
    for i in range(len(dartResult)):
        if dartResult[i] in nums:
            if dartResult[i] == '1' and dartResult[i + 1] == '0' or dartResult[i - 1] == '1' and dartResult[i] == '0':
                current_num = 10
                
            else:
                current_num = int(dartResult[i])
            
        if dartResult[i] in bonuses.keys():
            result.append(current_num ** bonuses[dartResult[i]])
            
        if dartResult[i] == '*':
            result[-1] *= 2
            
            if i != 2:
                result[-2] *= 2

        elif dartResult[i] == '#':
            result[-1] *= -1
            
    return sum(result)