class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)
        rep=n//3
        nums.sort()
        occ=1
        res=[]
        if n==1:
            return nums
        for i in range(1,n):
            if nums[i]==nums[i-1]:
                occ+=1
            else:
                if occ>rep:
                    res.append(nums[i-1])
                occ=1
        if occ>rep:
            res.append(nums[-1])
        return res
        