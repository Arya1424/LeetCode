class KthLargest(object):

    def __init__(self, k, nums):
        self.k=k
        self.nums=sorted(nums,reverse=True)
    
    def add(self, val):
        index=0
        while index<len(self.nums) and self.nums[index]>val:
            index+=1
        self.nums.insert(index,val)
        return self.nums[self.k-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)