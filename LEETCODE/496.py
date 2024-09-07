class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        arr = []
        nums2 = sorted(nums2)
        for n in nums1:
            
            if(nums2.index(n) != len(nums2)-1):
                print(n)
                arr.append(nums2[nums2.index(n)+1])
            else:
                arr.append(-1)
        print(arr)
Solution().nextGreaterElement([4,1,2],[1,3,4,2])