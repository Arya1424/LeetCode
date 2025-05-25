class Solution(object):
    def maxArea(self, height):
        maxvol=0
        left=0
        right=len(height)-1
        while left<right:
            vol=min(height[left],height[right])*(right-left)
            if vol>maxvol:
                maxvol=vol 
            if height[left]<height[right]:
                left+=1
            else:
                right-=1                 
        return maxvol
        