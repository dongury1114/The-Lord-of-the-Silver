class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = list()
        
        def _check(target, nums2):
            left = 0
            right = len(nums2) - 1
            nums2.sort()
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums2[mid] == target:
                    return target
                
                elif nums2[mid] > target:
                    right = mid - 1
                
                elif nums2[mid] < target:
                    left = mid + 1
        
        for i in nums1:
            tmp = _check(i, nums2)
            
            if tmp != None and tmp not in result:
                result.append(tmp)
                
        return result