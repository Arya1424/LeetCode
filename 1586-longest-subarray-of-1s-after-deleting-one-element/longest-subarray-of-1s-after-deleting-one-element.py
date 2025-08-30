class Solution(object):
    def longestSubarray(self, nums):
        max_w=0
        l=0
        num_z=0
        for r in range(len(nums)):
            if nums[r]==0:
                num_z+=1
            while num_z>1:
                if nums[l]==0:
                    num_z-=1
                l+=1
            max_w=max(max_w,r-l)
        return max_w

        