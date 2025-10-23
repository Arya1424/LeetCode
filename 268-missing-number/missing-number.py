class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        m=[0]*(len(nums)+1)
        for i in nums:
            m[i]=1
        return m.index(0)
        