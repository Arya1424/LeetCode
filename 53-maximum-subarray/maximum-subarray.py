class Solution(object):
    def maxSubArray(self, nums):
        current=nums[0]
        maxsum=nums[0]
        start,end=0,0
        temp=0
        for i in range(1,len(nums)):
            if nums[i]>current+nums[i]:
                current=nums[i]
                temp=i
            else:
                current+=nums[i]
            if current>maxsum:
                maxsum=current
                start=i
                end=i
        return maxsum
