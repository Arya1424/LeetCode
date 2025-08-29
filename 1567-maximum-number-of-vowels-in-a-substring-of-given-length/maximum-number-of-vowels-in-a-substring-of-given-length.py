class Solution(object):
    def maxVowels(self, s, k):
        vow=0
        for i in range(k):
            if s[i] in "aeiou":
                vow+=1
        max_vow=vow
        for i in range(k,len(s)):
            if s[i-k] in "aeiou":
                vow-=1
            if s[i] in "aeiou":
                vow+=1
            max_vow=max(max_vow,vow)
        return max_vow
        