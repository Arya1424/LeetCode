class Solution(object):
    def maxArea(self, height):
        l,r=0,len(height)-1
        water=0
        while l<r:
            cont=min(height[l],height[r])*(r-l)
            water=max(water,cont)
            if height[l]>height[r]:
                r-=1
            else:
                l+=1

        return water
