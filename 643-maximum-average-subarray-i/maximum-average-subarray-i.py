class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l, r=0, k-1
        s=sum(nums[l:r+1])
        max_avg=s/k
        while r+1<len(nums):
            s-=nums[l]
            l+=1
            r+=1
            s+=nums[r]
            max_avg=max(max_avg, s/k)

        return max_avg
