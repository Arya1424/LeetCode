class Solution(object):
    def distributeCandies(self, candyType):
        n=len(candyType)/2
        types=set()
        for i in candyType:
            types.add(i)
        candy=len(types)
        if candy>n:
            return n
        else:
            return candy