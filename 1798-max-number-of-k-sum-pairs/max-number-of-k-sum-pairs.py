class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count=0
        l, r=0, len(nums)-1
        while l<r:
            s=nums[l]+nums[r]
            if s==k:
                count+=1
                r-=1
                l+=1
            elif s>k:
                r-=1
            else:
                l+=1
        return count
