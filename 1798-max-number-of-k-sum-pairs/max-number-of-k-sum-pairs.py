class Solution(object):
    def maxOperations(self, nums, k):
        i,j=0,len(nums)-1
        res=0
        nums.sort()
        while i<j:
            temp=nums[i]+nums[j]
            if temp==k:
                res+=1
                i+=1
                j-=1
            elif temp>k:
                j-=1
            else:
                i+=1
        return res
        