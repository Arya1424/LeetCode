class Solution(object):
    def findErrorNums(self, nums):
        n=len(nums)
        count=[0]*(n+1)
        for i in nums:
            count[i]+=1
        for i in range(len(count)):
            if count[i]==2:
                dup=i
            elif count[i]==0:
                miss=i
        return [dup,miss]


        