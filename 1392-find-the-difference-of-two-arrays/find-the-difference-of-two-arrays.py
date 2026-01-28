class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        diff1=[]
        nums1=set(nums1)
        nums2=set(nums2)
        for i in nums1:
            if i not in nums2:
                diff1.append(i)
        diff2=[]
        for i in nums2:
            if i not in nums1:
                diff2.append(i)

        res=[]
        res.append(diff1)
        res.append(diff2)
        return res