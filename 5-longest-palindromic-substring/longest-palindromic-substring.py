class Solution(object):
    def longestPalindrome(self, s):
        if not s or len(s)<1:
            return ""
        start=end=0
        def wrap(left,right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return right-left-1
        for i in range(len(s)):
            len1=wrap(i,i)
            len2=wrap(i,i+1)
            maxlen=max(len1,len2)

            if maxlen>end-start:
                start=i-(maxlen-1)//2
                end=i+(maxlen)//2
        return s[start:end+1]

            
        