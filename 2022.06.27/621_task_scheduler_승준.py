class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_count = collections.Counter(tasks)
        maxheap = list()
        total_count = 0
        
        for key, value in tasks_count.items():
            heappush(maxheap, (-value, key))
        
        while maxheap:
            current_interval = 0
            temps = list()
            
            while current_interval <= n:
                total_count += 1
                
                if maxheap:
                    value, key = heappop(maxheap)
                    
                    if value != -1:
                        temps.append([value + 1, key])
                        
                if not maxheap and not temps:
                    break
                    
                else:
                    current_interval += 1
                    
            for temp in temps:
                heappush(maxheap, (temp[0], temp[1]))
                
        return total_count
                
        