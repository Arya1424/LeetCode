class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        new=[i+extraCandies for i in candies]
        res=[]
        m=max(candies)
        for i in range(len(candies)):
            if new[i]>=m:
                res.append(True)
            else:
                res.append(False)
        return res
        