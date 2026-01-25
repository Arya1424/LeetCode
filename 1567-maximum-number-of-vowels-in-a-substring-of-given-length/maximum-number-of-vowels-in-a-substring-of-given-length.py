class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels="aeiou"
        count=0
        for i in range(k):
            if s[i] in vowels:
                count+=1

        maxcount=count
        l, r=0, k-1
        while r+1<len(s):
            if s[l] in vowels:
                count-=1
            l+=1
            r+=1
            if s[r] in vowels:
                count+=1
            maxcount=max(count, maxcount)

        return maxcount 
