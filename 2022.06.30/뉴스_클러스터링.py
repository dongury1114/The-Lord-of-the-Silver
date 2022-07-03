from collections import Counter

def solution(str1, str2):
    str1_alpha = list()
    str2_alpha = list()
    
    for i in range(len(str1) - 1):
        if (str1[i:i + 2].lower()).isalpha():
            str1_alpha.append(str1[i:i + 2].lower())
            
    for i in range(len(str2) - 1):
        if (str2[i:i + 2].lower()).isalpha():
            str2_alpha.append(str2[i:i + 2].lower())
            
    str1_counter = Counter(str1_alpha)
    str2_counter = Counter(str2_alpha)
    
    def _intersection(a, b):
        result = 0
        
        temp_a = a.keys()
        temp_b = b.keys()
        
        for key in temp_a:
            if key in temp_b:
                result += min(a[key], b[key])
                
        return result
    
    def _union(a, b):
        result = 0
        
        temp_a = a.keys()
        temp_b = b.keys()
        
        for key in temp_a:
            if key in temp_b:
                result += max(a[key], b[key])
                
            else:
                result += a[key]
                
        for key in temp_b:
            if key in temp_a:
                continue
            
            else:
                result += b[key]
                
        return result
    
    intersection = _intersection(str1_counter, str2_counter)
    union = _union(str1_counter, str2_counter)
    
    if intersection == 0 and union == 0:
        return 65536
    
    else:
        return int((intersection / union) * 65536)    