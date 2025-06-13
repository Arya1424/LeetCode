class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1+=nums2
        nums1.sort()
        z=len(nums1)-(m+n)
        for i in range(z):
            nums1.remove(0)
        