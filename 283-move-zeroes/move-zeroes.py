class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pos=0
        for i in nums:
            if i!=0:
                nums[pos]=i
                pos+=1

        while pos<len(nums):
            nums[pos]=0
            pos+=1
        