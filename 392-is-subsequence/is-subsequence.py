class Solution(object):
    def isSubsequence(self, s, t):
        l1,l2=0,0
        while l1<len(s) and l2<len(t):
            if s[l1]==t[l2]:
                l1+=1
                l2+=1
            else:
                l2+=1
        if l1==len(s):
            return True
        return False
        