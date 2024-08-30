from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        resp = []
        if(len(nums1) <= len(nums2)):
            for c in range(0, len(nums1)):
                if(nums1[c] in nums2):
                    resp.append(nums1[c])    
                    nums2.pop(nums2.index(nums1[c]))
        else:
            for c in range(0, len(nums2)):
                if(nums2[c] in nums1):
                    resp.append(nums2[c])  
                    nums1.pop(nums1.index(nums2[c]))
        return resp
    
print(Solution().intersect([3,1,2],[1,1]))