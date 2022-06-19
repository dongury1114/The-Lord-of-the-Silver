class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import defaultdict
        dic = defaultdict(list)
        result = []
        for n in list(set(nums1))+list(set(nums2)):
            dic[n].append(1)
        for key, value in dic.items():
            if len(value) > 1:
                result.append(key)
        return(result)
