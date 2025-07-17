class Solution(object):
    def reverseWords(self, s):
        res=""
        l=s.split(" ")
        i=len(l)-1
        while i>=0:
            if l[i]:
                res+=" "+l[i]
            i-=1
        return res.strip()