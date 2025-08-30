class Solution(object):
    def pivotIndex(self, nums):
        left_sum=0
        s=sum(nums)
        for i,num in enumerate(nums):
            if left_sum==s-left_sum-num:
                return i
            left_sum+=num
        return -1