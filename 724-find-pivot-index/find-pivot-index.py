class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left=0
        s=sum(nums)
        for i, num in enumerate(nums):
            if left==s-left-num:
                return i
            left+=num
        return -1