class Solution(object):
    def lengthOfLongestSubstring(self, s):
        #sliding window
        l=0
        se=set()
        longest=0

        for r in range(len(s)):
            while s[r] in se:
                se.remove(s[l])
                l+=1
            wl=r-l+1
            longest=max(longest,wl)
            se.add(s[r])
        return longest