class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        l,r=0,1
        while l<r and r<len(prices):
            profit=prices[r]-prices[l]
            if profit<0:
                l=r
            else:
                maxprofit=max(maxprofit, profit)
            r+=1
        return maxprofit
        