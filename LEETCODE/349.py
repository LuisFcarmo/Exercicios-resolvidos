class Solution:
    def intersection(self, nums1, nums2):
        n1 = set()
        n2 = set()
        for n in nums1:
            n1.add(n)
        for n in nums2:
            n2.add(n)
        return n1.intersection(n2)