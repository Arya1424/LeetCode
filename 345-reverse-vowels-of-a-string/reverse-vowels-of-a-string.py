class Solution(object):
    def reverseVowels(self, s):
        v=[]
        for i in s:
            if i in "AEIOUaeiou":
                v+=i
        v.reverse()
        j=0
        for i in range(len(s)):
            if s[i] in "AEIOUaeiou":
                s=s[:i] +v[j]+s[i+1:]
                j+=1
        return s

        