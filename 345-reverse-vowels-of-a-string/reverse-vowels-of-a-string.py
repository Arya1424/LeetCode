class Solution(object):
    def reverseVowels(self, s):
        strlist=list(s)
        l,r=0,len(s)-1
        while l<r:
            while l<r and strlist[l] not in "AEIOUaeiou":
                l+=1
            while l<r and strlist[r] not in "AEIOUaeiou":
                r-=1
            strlist[l],strlist[r]=strlist[r],strlist[l]
            l+=1
            r-=1
        return "".join(strlist)

        

        