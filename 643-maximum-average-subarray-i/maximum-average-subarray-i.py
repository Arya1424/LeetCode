class Solution(object):
    def findMaxAverage(self, nums, k):
        n=len(nums)
        curr=0

        for i in range(k):
            curr+=nums[i]
        maxavg=float(curr)/k

        for i in range(k,n):
            curr+=nums[i]
            curr-=nums[i-k]

            avg=float(curr)/k
            maxavg=max(maxavg,avg)
        return maxavg

