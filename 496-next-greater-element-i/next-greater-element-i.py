class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        idx={n:i for i, n in enumerate(nums1)}
        res=[-1]*len(nums1)
        stack=[]

        for i in range(len(nums2)):
            cur=nums2[i]
            while stack and cur>stack[-1]:
                val=stack.pop()
                index=idx[val]
                res[index]=cur
            if cur in idx:
                stack.append(cur)
        return res
                