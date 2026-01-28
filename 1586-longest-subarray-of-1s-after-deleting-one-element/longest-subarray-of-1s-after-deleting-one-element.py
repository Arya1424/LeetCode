class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=0
        maxlen=0
        flag=False
        for r in range(len(nums)):
            if nums[r]==0:
                if not flag:
                    flag=True
                else:
                    while nums[l]==1:
                        l+=1
                    l+=1
            maxlen=max(maxlen, r-l)

        return maxlen
            
            
