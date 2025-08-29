class Solution(object):
    def findMaxAverage(self, nums, k):
        max_sum=sum(nums[:k])
        s=max_sum
        for i in range(k,len(nums)):
            s+=nums[i]-nums[i-k]
            max_sum=max(s,max_sum)
        
        return float(max_sum)/k
        