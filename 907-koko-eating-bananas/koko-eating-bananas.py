class Solution(object):
    def minEatingSpeed(self, piles, h):
        l,r=1,max(piles)
        res=r
        while l<=r:
            mid=(l+r)//2
            t=0
            for i in piles:
                t+=math.ceil(float(i)/mid)
            if t<=h:
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res

        