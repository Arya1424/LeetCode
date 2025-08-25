class Solution(object):
    def mergeAlternately(self, word1, word2):
        res=""
        i=0
        while i<len(word1) and i<len(word2):
            res+=(word1[i])
            res+=(word2[i])
            i+=1
        
        while i<len(word1):
            res+=(word1[i])
            i+=1
        
        while i<len(word2):
            res+=(word2[i])
            i+=1
        
        return res