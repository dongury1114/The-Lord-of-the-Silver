from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    
    def lower(x):
        return x.lower()
    
    cities = list(map(lower, cities))
    cache = deque()
    result = 0
    
    for city in cities:
        if city in cache:
            cache.remove(city)
            cache.append(city)
            result += 1
            
        else:
            result += 5
            
            if len(cache) == cacheSize:
                cache.popleft()
                cache.append(city)
                
            else:
                cache.append(city)

    return result
    