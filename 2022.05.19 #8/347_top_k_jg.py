class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = collections.Counter(nums)
        
        print(cnt.most_common())
        result=[]
        for i in cnt.most_common()[:k]:
            result.append(i[0])
        return result
