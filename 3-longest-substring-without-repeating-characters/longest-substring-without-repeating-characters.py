class Solution(object):
    def lengthOfLongestSubstring(self, s):
        #sliding window
        charset=set()
        left=0
        maxlen=0
        for right in range(len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                left+=1
            charset.add(s[right])
            maxlen=max(maxlen,right-left+1)
        return maxlen

