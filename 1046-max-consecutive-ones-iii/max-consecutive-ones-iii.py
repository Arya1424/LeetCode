class Solution(object):
    def longestOnes(self, nums, k):
        max_w=0
        l=0
        num_z=0
        for r in range(len(nums)):
            if nums[r]==0:
                num_z+=1
            while num_z>k:
                if nums[l]==0:
                    num_z-=1
                l+=1
            max_w=max(max_w,r-l+1)
        return max_w


        