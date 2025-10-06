class Solution(object):
    def tribonacci(self, n):
        tri=[0,1,1]
        if n<3:
            return tri[n]
        for i in range(3,n+1):
            tri.append(tri[i-1]+tri[i-2]+tri[i-3])
        return tri[-1]

        