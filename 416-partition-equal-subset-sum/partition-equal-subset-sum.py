class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2==1:
            return False

        n=len(nums)
        dp=set()
        dp.add(0)
        target=sum(nums)//2

        for i in range(n-1,-1,-1):
            nextDp=set()
            for t in dp:
                nextDp.add(nums[i]+t)
                nextDp.add(t)

            dp=nextDp
        return True if target in dp else False