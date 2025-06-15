class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxone=0
        occ=0
        for i in nums:
            if i==1:
                occ+=1
                maxone=max(maxone,occ)
            else:
                occ=0
        return maxone
        