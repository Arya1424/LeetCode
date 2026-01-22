class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r=0, len(height)-1
        maxwater=0
        while l<r:
            water=(r-l)*min(height[l], height[r])
            maxwater=max(water, maxwater)
            if height[l]>height[r]:
                r-=1
            else:
                l+=1             

        return maxwater
