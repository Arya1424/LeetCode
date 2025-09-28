class Solution(object):
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        m=len(potions)
        res=[]
        for i in spells:
            l,r=0,m
            while l<r:
                mid=(l+r)//2
                if i*potions[mid]>=success:
                    r=mid
                else:
                    l=mid+1
            res.append(m-l)
        return res

        