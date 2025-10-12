class Solution(object):
    def numTilings(self, n):
        mod=10**9+7
        if n==0:
            return 1
        if n==1:
            return 1
        if n==2:
            return 2
        f0,f1,f2=1,1,2
        g0,g1=0,1

        for i in range(3,n+1):
            f_new=(f1+f2+2*g1)%mod
            g_new=(g1+f1)%mod

            f0,f1,f2=f1,f2,f_new
            g0,g1=g1,g_new
        return f2