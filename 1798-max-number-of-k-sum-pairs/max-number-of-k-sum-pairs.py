class Solution(object):
    def maxOperations(self, nums, k):
        m={}
        res=0
        for i in nums:
            diff=k-i
            if diff in m and m[diff]>0:
                res+=1
                m[diff]-=1
            else:
                m[i]=m.get(i,0)+1
        return res

        