class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        count,i,size=0,0,len(flowerbed)

        while i<size:
            if (flowerbed[i]==0 and (i==0 or flowerbed[i-1]==0) and (i==size-1 or flowerbed[i+1]==0)):
                count+=1
                i+=2
            else:
                i+=1
            if count>=n:
                return True
        return False

        
        