class Solution(object):
    def isPalindrome(self, s):
        l,r=0,len(s)-1
        while l<=r:
            while l<r and not s[l].isalnum():
                l+=1
            while l<r and not s[r].isalnum():
                r-=1
            if s[l].lower()==s[r].lower():
                r-=1
                l+=1
            else:
                return False
        return True