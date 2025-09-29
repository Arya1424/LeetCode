class Solution(object):
    def findPeakElement(self, nums):
        s=sorted(nums)
        return nums.index(s[-1])
        